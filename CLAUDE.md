# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

CV generation system that produces a PDF and a SvelteKit web app from a single YAML source (`resume.yml`). Pipeline: YAML → Jinja2 → LaTeX → PDF, with a separate web build.

## Prerequisites (must be installed before running anything)

### PDF generation
- **Python 3** — `python --version` or `python3 --version`
- **xelatex** — required to compile LaTeX to PDF
  - **Windows**: Install [MiKTeX](https://miktex.org/download). During install, choose "Install missing packages on the fly". After install, open MiKTeX Console and run "Check for updates". Verify with `xelatex --version` in a new terminal.
  - **macOS**: `brew install --cask mactex` or install [MacTeX](https://www.tug.org/mactex/)
  - **Linux**: `sudo apt install texlive-xetex texlive-fonts-recommended texlive-fonts-extra`

### Web app
- **Node.js** (v18+) and **npm** — `node --version` and `npm --version`

### Windows-specific
- Run all `make` commands in **Git Bash** (not PowerShell or CMD). Git Bash ships with Git for Windows.
- Verify `make` is available: `make --version`. If not, install via [GnuWin32](https://gnuwin32.sourceforge.net/packages/make.htm) or use `winget install GnuWin32.Make`.

## Build Commands

All build operations use `make` from the project root (run in Git Bash on Windows):

```bash
make              # Full pipeline: install → validate → generate → compile → markdown
make install      # Install Python dependencies
make validate     # Validate resume.yml against schema.json + check template syntax
make generate     # Render template.jinja → tex/resume.tex
make compile      # xelatex compile → out/Alicia-Sykes-CV.pdf
make markdown     # Generate → out/Alicia-Sykes-CV.md
make clean        # Remove all generated output files
make watch        # Watch for changes and rebuild (requires `entr`)
```

Web app:

```bash
make web_dev      # Start dev server at http://localhost:5173
make web          # Build + preview (output in web/.svelte-kit/output/)
make web_install  # Install Node deps only
```

Web linting (run from `web/`):

```bash
npm run lint      # Prettier check + ESLint
npm run format    # Auto-format with Prettier
npm run check     # TypeScript + Svelte type check
```

## Quick Start (first time)

```bash
# 1. Install Python deps
make install

# 2. Edit your CV data
# Open resume.yml and replace content with your own

# 3. Validate your data
make validate

# 4. Generate LaTeX + compile PDF
make generate
make compile
# Output: out/Alicia-Sykes-CV.pdf

# 5. (Optional) Web app
make web_dev
```

## Architecture

**Single source of truth:** `resume.yml` — all outputs derive from this file.

**PDF pipeline:**
1. `lib/validate.py` — validates `resume.yml` against `schema.json` and Jinja2 template syntax
2. `lib/generate.py` — renders `template.jinja` with YAML data → writes `tex/resume.tex`
3. `lib/compile.py` — runs `xelatex` on `tex/resume.tex` → `out/Alicia-Sykes-CV.pdf`
4. `lib/markdown.py` — generates `out/Alicia-Sykes-CV.md` from YAML

**LaTeX layer:** `tex/resume-format.cls` is the custom document class. Fonts live in `tex/fonts/`. FontAwesome icons via `tex/fontawesome.sty`. The `tex/resume.tex` file is auto-generated — do not edit it directly.

**Jinja2 template** (`template.jinja`) uses custom filters: `latex_escape`, `format_date`, `markdown_to_latex`.

**Web app** (`web/`): SvelteKit with multi-page routing. Dual adapter — static for GitHub Pages (`GITHUB_PAGES` env var), auto otherwise.

## Key Files to Edit

| File | Purpose |
|------|---------|
| `resume.yml` | All CV content (edit this) |
| `template.jinja` | LaTeX layout/structure |
| `tex/resume-format.cls` | PDF styling and formatting |
| `web/src/` | Web app components and pages |

## CI/CD Workflows

| Workflow | Trigger | What it does |
|----------|---------|--------------|
| `validate.yml` | PR to main | Runs `make validate` |
| `build-site.yml` | Push to main / PR | Builds PDF + SvelteKit, deploys to `website` branch |
| `compile.yml` | Tag push / manual | Builds PDF, creates GitHub Release |
| `tag.yml` | Manual dispatch | Bumps sem ver patch tag |
