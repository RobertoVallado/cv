# Roberto Vallado — CV

Personal CV system. One file to rule them all: **[`resume.yml`](resume.yml)** is the single source of truth. Editing it updates the PDF, the live website, and all language versions automatically.

**Live site:** [cv.robertovallado.dev](https://cv.robertovallado.dev)

---

## System overview

```
resume.yml  ← the only file you need to edit
    │
    ├── lib/generate.py --lang en ──→ tex/resume.tex → out/Roberto-Vallado-CV-EN.pdf
    ├── lib/generate.py --lang fr ──→ tex/resume.tex → out/Roberto-Vallado-CV-FR.pdf
    │
    └── web/  (SvelteKit static site)
          ├── +layout.server.ts   reads resume.yml at build/dev time
          ├── +page.server.ts     home page — full resume data
          ├── experience/         job highlights (EN + FR from resume.yml)
          ├── skills/             skill groups from resume.yml
          └── achievements, contact, intro, ideal-role  (i18n JSON)
```

Push to `main` → GitHub Actions builds the PDF and deploys the site to GitHub Pages. Done.

---

## Editing your CV

Everything lives in `resume.yml`. Open it, make changes, push.

```bash
git add resume.yml
git commit -m "update cv"
git push
```

The site and PDF rebuild automatically. The live site updates in a few minutes.

### Key sections in resume.yml

| Section | What it controls |
|---|---|
| `basics` | Name, headline, email, GitHub URL, LinkedIn, location |
| `personal-statement` | The summary paragraph on the home page and PDF |
| `personal-statement-fr` | French version of the summary |
| `work` | Job entries — each has `position`, `highlights`, and `highlights-fr` |
| `education` | Degrees and diplomas |
| `skills` | Skill groups shown on the Skills page and PDF |
| `achievements` | Bullet points on the Achievements page and PDF |
| `awards` | Awards listed on Achievements and PDF |

### Bilingual content (EN / FR)

The site has a language toggle in the top-right header. French content is sourced from:
- `personal-statement-fr` in resume.yml
- `position-fr` and `highlights-fr` on each work entry
- `web/src/lib/locales/fr.json` for all UI strings, page text, soft skills, achievements stats

To add or update French content, edit either the `*-fr` fields in `resume.yml` or the `fr.json` locale file.

### Adding a new translation key

1. Add the key + English value to `web/src/lib/locales/en.json`
2. Add the French translation to `web/src/lib/locales/fr.json`
3. Use `$t('your.key')` in the Svelte component

---

## Local development

### Prerequisites

| Tool | Version | Purpose |
|---|---|---|
| Python | 3.11+ | PDF pipeline |
| Node.js | 20+ | Web dev server |
| MiKTeX / TeX Live | latest | XeLaTeX (PDF only) |

### Web dev server

The web app reads `resume.yml` directly from the project root at dev time — no GitHub push needed to see your changes.

```bash
cd web
npm install
npm run dev        # http://localhost:5173
```

Edit `resume.yml`, save, refresh — changes appear immediately.

### PDF generation

The generator supports `--lang en` and `--lang fr`. Both PDFs are built from the same `resume.yml` — French fields (`personal-statement-fr`, `position-fr`, `highlights-fr`, etc.) are swapped in automatically when `--lang fr` is used.

```bash
pip install -r lib/requirements.txt

# English PDF
python lib/generate.py \
  --resume resume.yml --template template.jinja \
  --output tex/resume.tex --lang en
python lib/compile.py \
  --input tex/resume.tex --output out/Roberto-Vallado-CV-EN.pdf

# French PDF
python lib/generate.py \
  --resume resume.yml --template template.jinja \
  --output tex/resume.tex --lang fr
python lib/compile.py \
  --input tex/resume.tex --output out/Roberto-Vallado-CV-FR.pdf
```

Or via Make:

```bash
make pdf        # builds both EN and FR
make pdf-en     # English only
make pdf-fr     # French only
```

**Windows note:** MiKTeX must be in PATH. If `xelatex` is not found, add it manually for your session:
```powershell
$env:PATH = "C:\Program Files\MiKTeX\miktex\bin\x64;$env:PATH"
```

### Validate resume.yml

```bash
python lib/validate.py --resume resume.yml --schema schema.json
```

### Production build (local preview)

```bash
cd web
GITHUB_PAGES=true npm run build
npm run preview
```

---

## Repository structure

```
resume.yml              Single source of truth — edit this
schema.json             JSON Schema for validating resume.yml
template.jinja          Jinja2 → LaTeX CV template
Makefile                Shortcuts for local builds

lib/
  generate.py           Renders template.jinja → LaTeX; --lang en|fr switches language
  compile.py            Compiles LaTeX → PDF via XeLaTeX
  validate.py           Validates resume.yml against schema.json
  markdown.py           Exports resume.yml → Markdown
  requirements.txt      Python deps (PyYAML, Jinja2, jsonschema, colorama)

tex/
  resume-format.cls     Custom LaTeX class (dark header, typography, layout)
  fontawesome.sty        FontAwesome icon support
  fonts/                Roboto font family (used in PDF)

out/
  Roberto-Vallado-CV-EN.pdf  English PDF (generated)
  Roberto-Vallado-CV-FR.pdf  French PDF (generated)

web/
  src/
    lib/
      i18n.ts             Custom i18n store — no library, locale-aware $t() function
      locales/en.json     English UI strings, page content, soft skills, achievements
      locales/fr.json     French translations
    routes/
      +layout.server.ts   Reads resume.yml → passes basics to layout
      +layout.svelte      Sidebar, nav, language toggle (EN/FR)
      +page.server.ts     Reads full resume.yml → home page
      +page.svelte        Home — summary view of all CV sections
      intro/              Personal bio (fully i18n)
      experience/         Job history — reads highlights-fr from resume.yml
      skills/             Skill groups + Language badge component
      achievements/       Stats, awards (fully i18n)
      contact/            Contact info (fully i18n)
      ideal-role/         Role preferences (fully i18n)
      download/           PDF download redirect
    components/
      Language.svelte     Tech badge with SimpleIcons — 50+ languages configured
    styles/
      variables.scss      Color palette (forest green dark theme)
      page-global.scss    Layout, sidebar, header
      link.scss           Buttons, links
      resume-main.scss    Home page resume styles
  svelte.config.js        Static adapter config (base path '' for custom domain)

.github/workflows/
  build-site.yml          Build PDF + SvelteKit → deploy to GitHub Pages
  validate.yml            Validate resume.yml on pull requests
```

---

## How the web app works

### Data flow

All page data is loaded **server-side at build time** (SvelteKit `+page.server.ts` with `prerender = true`). This means:
- `resume.yml` is read directly from the filesystem during `npm run dev` and `npm run build`
- No network calls to GitHub at runtime
- Changes to `resume.yml` are reflected immediately in `npm run dev`

### i18n

The language system (`src/lib/i18n.ts`) is a lightweight custom store — no library dependency:
- `$t('key')` — returns the translated value for the active locale
- `setLocale('fr')` — switches locale, persists to `localStorage`
- Falls back to English for any missing French key
- Arrays and objects (soft skills, requirements, stats) are stored in the JSON files and accessed reactively

### Theme

Dark theme using Roberto's personal brand green palette:
- `--primary: #22a866` (forest green — from robertovallado.dev)
- `--secondary: #5a9e7e`
- `--background: #0b0f0c` (deep dark with warm undertone)
- Font: Fira Mono throughout

---

## CI / Deployment

The `build-site.yml` workflow triggers on push to `main` when `web/**`, `resume.yml`, or the workflow itself changes.

**What it does:**
1. Installs Python + LaTeX, generates and compiles the PDF
2. Installs Node.js, builds the SvelteKit static site
3. Copies both PDFs into the site build as `roberto-vallado-cv-en.pdf` and `roberto-vallado-cv-fr.pdf`
4. Writes a `CNAME` file (`cv.robertovallado.dev`) into the build output
5. Deploys to GitHub Pages via `actions/deploy-pages`

**One-time setup required:** `Settings → Pages → Source → GitHub Actions`

### Custom domain DNS

| Type | Name | Value |
|---|---|---|
| `CNAME` | `cv` | `robertovallado.github.io` |

Then go to `Settings → Pages → Custom domain` → enter `cv.robertovallado.dev` → enable **Enforce HTTPS**.

---

## License

Forked from [lissy93/cv](https://github.com/Lissy93/cv) by Alicia Sykes, MIT licensed. See [`LICENSE`](LICENSE).
