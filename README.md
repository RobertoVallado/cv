# CV

CV generation system — produces a PDF and interactive web app from a single YAML file.

See [`.github/README.md`](.github/README.md) for full documentation.

## Quick Start

### Prerequisites

- **Python 3** and **pip**
- **xelatex**:
  - Windows: Install [MiKTeX](https://miktex.org/download), then run MiKTeX Console and check for updates
  - macOS: `brew install --cask mactex`
  - Linux: `sudo apt install texlive-xetex texlive-fonts-recommended texlive-fonts-extra`
- **make** (Windows: use Git Bash)

### Generate PDF

```bash
make install    # Install Python deps
# Edit resume.yml with your content
make            # Validate → generate LaTeX → compile PDF → markdown
# Output: out/Alicia-Sykes-CV.pdf
```

### Web app

```bash
make web_dev    # http://localhost:5173
```

## Editing

- **`resume.yml`** — all CV content lives here
- **`template.jinja`** — LaTeX layout
- **`tex/resume-format.cls`** — PDF styling
- **`web/src/`** — web app
