# Roberto Vallado — CV

Personal CV system with a single source of truth and bilingual (EN/FR) output across both PDF and website.

**Live site:** [cv.robertovallado.dev](https://cv.robertovallado.dev)

---

## System overview

```
resume.yml  ← edit this to update most content
    │
    ├── PDF pipeline
    │     ├── lib/generate.py --lang en → tex/resume.tex → Roberto-Vallado-CV-EN.pdf
    │     └── lib/generate.py --lang fr → tex/resume.tex → Roberto-Vallado-CV-FR.pdf
    │           (French fields: personal-statement-fr, position-fr, highlights-fr,
    │            text-fr on achievements, summary-fr on awards)
    │
    └── SvelteKit web (web/)
          ├── server-side loads — read resume.yml directly at build/dev time
          │     ├── +layout.server.ts  → basics (name, headline, social links)
          │     ├── +page.server.ts    → full resume data (home page)
          │     ├── experience/        → work entries + highlights-fr
          │     └── skills/            → skill groups
          │
          └── i18n JSON — web/src/lib/locales/
                ├── en.json  → intro bio, achievements page, contact,
                │              ideal-role, soft skills, all UI labels
                └── fr.json  → French translations of all the above
```

Push to `main` → GitHub Actions builds both PDFs and deploys the site. Done.

---

## Content sources at a glance

| What | Where to edit | Affects |
|---|---|---|
| Name, headline, email, links | `resume.yml` → `basics` | Sidebar, home page, PDF header |
| Personal summary (EN) | `resume.yml` → `personal-statement` | Home page, PDF |
| Personal summary (FR) | `resume.yml` → `personal-statement-fr` | Home page (FR), FR PDF |
| Job history (EN) | `resume.yml` → `work[].highlights` | Home page, Experience page, PDF |
| Job history (FR) | `resume.yml` → `work[].highlights-fr` | Experience page (FR), FR PDF |
| Skills | `resume.yml` → `skills` | Home page, Skills page, PDF |
| Home page achievements | `resume.yml` → `achievements` | Home page, PDF |
| /achievements page stats | `web/src/lib/locales/en.json` → `achievements.stats` | Achievements page only |
| /achievements page (FR) | `web/src/lib/locales/fr.json` → `achievements.stats` | Achievements page (FR) only |
| Intro bio | `web/src/lib/locales/*.json` → `intro.p0–p5` | Intro page |
| Contact text | `web/src/lib/locales/*.json` → `contact.*` | Contact page |
| Ideal role text | `web/src/lib/locales/*.json` → `ideal_role.*` | Ideal Role page |
| All nav / UI labels | `web/src/lib/locales/*.json` → `nav.*` | Everywhere |

> **Note:** The `/achievements` page and the home page achievements section have separate content sources. Update both `resume.yml` achievements and the i18n JSON stats when changing achievements content.

---

## Editing your CV

For most changes, edit `resume.yml` and push:

```bash
git add resume.yml
git commit -m "update cv"
git push
```

For narrative page content (intro bio, contact text, ideal role, achievements page):

```bash
# edit web/src/lib/locales/en.json  (English)
# edit web/src/lib/locales/fr.json  (French)
git add web/src/lib/locales/
git commit -m "update page content"
git push
```

The site and PDFs rebuild automatically on push. Live in a few minutes.

---

## Bilingual content (EN / FR)

The site has an **EN / FR** toggle in the top-right header. Locale is saved to `localStorage`.

**In `resume.yml`**, French variants are parallel fields:
- `personal-statement-fr` — French personal summary
- `work[].position-fr` — French job title
- `work[].highlights-fr` — French bullet points
- `achievements[].text-fr` — French achievement text
- `awards[].summary-fr` — French award summary

**In the i18n JSON** (`web/src/lib/locales/fr.json`), every key in `en.json` has a French counterpart. Falls back to English for any missing key.

### Adding a new translation key

1. Add key + English value to `web/src/lib/locales/en.json`
2. Add French translation to `web/src/lib/locales/fr.json`
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

The web app reads `resume.yml` directly from the filesystem — no push to GitHub needed.

```bash
cd web
npm install
npm run dev        # http://localhost:5173
```

Edit `resume.yml` or the i18n JSON files, save, refresh — changes appear immediately.

### PDF generation

Both PDFs are built from the same `resume.yml`. French fields are swapped in automatically by `generate.py` when `--lang fr` is used.

```bash
pip install -r lib/requirements.txt

# English PDF
python lib/generate.py --resume resume.yml --template template.jinja \
  --output tex/resume.tex --lang en
python lib/compile.py --input tex/resume.tex --output out/Roberto-Vallado-CV-EN.pdf

# French PDF
python lib/generate.py --resume resume.yml --template template.jinja \
  --output tex/resume.tex --lang fr
python lib/compile.py --input tex/resume.tex --output out/Roberto-Vallado-CV-FR.pdf
```

Or via Make:

```bash
make pdf        # builds both
make pdf-en     # English only
make pdf-fr     # French only
```

The Makefile also copies the PDFs to `web/static/` so the dev server can serve them for the Download button.

**Windows — MiKTeX not found:**
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
resume.yml              Single source of truth for resume data
schema.json             JSON Schema — validates resume.yml structure
template.jinja          Jinja2 template → LaTeX (locale-aware labels + content)
Makefile                Shortcuts: make pdf / pdf-en / pdf-fr / validate / clean

lib/
  generate.py           Renders template; --lang en|fr swaps French fields in
  compile.py            Runs XeLaTeX to produce PDF (timeout: 300s)
  validate.py           Validates resume.yml + template syntax
  markdown.py           Exports resume.yml → Markdown
  requirements.txt      PyYAML, Jinja2, jsonschema, colorama

tex/
  resume-format.cls     Custom LaTeX class (green header, fonts, layout commands)
  fontawesome.sty        FontAwesome icon support
  fonts/                Roboto font family

out/
  Roberto-Vallado-CV-EN.pdf   English PDF (generated)
  Roberto-Vallado-CV-FR.pdf   French PDF (generated)

web/
  src/
    lib/
      i18n.ts             Svelte store: $t(), setLocale(), locale — no npm dependency
      locales/en.json     All English strings + page content
      locales/fr.json     All French translations
    routes/
      +layout.server.ts   Reads resume.yml → basics → sidebar + header
      +layout.svelte      Sidebar, nav, EN/FR toggle button
      +page.server.ts     Reads resume.yml → all sections → home page
      +page.svelte        Home — summary view with links to each section
      intro/              Bio (fully i18n, no server load)
      experience/         Jobs from resume.yml, locale-aware highlights
      skills/             Skill groups from resume.yml + Language badge component
      achievements/       Stats + awards from i18n JSON (no server load)
      contact/            Contact (fully i18n, no server load)
      ideal-role/         Role preferences (fully i18n, no server load)
      download/           Triggers browser download of EN or FR PDF
    components/
      Language.svelte     Tech badge — SimpleIcons CDN, 50+ techs configured
    styles/
      variables.scss      Color palette (#22a866 forest green, dark backgrounds)
      page-global.scss    Layout, sidebar, header, responsive
      link.scss           Buttons (.download-btn, .big-btn, .small-btn), links
      resume-main.scss    Home page resume section styles
  svelte.config.js        Static adapter; base '' for custom domain (no /cv prefix)
  static/
    roberto-vallado-cv-en.pdf  Copied here by make pdf-en (gitignored)
    roberto-vallado-cv-fr.pdf  Copied here by make pdf-fr (gitignored)

.github/workflows/
  build-site.yml          Builds both PDFs → builds SvelteKit → deploys to GitHub Pages
  validate.yml            Validates resume.yml on every pull request
```

---

## CI / Deployment

`build-site.yml` runs on every push to `main` touching `web/**`, `resume.yml`, or the workflow file.

**Steps:**
1. Install Python + LaTeX; generate EN and FR PDFs from `resume.yml`
2. Install Node.js; build SvelteKit static site (reads `resume.yml` at build time)
3. Copy both PDFs into the build output
4. Write `CNAME` (`cv.robertovallado.dev`) into the build output
5. Deploy to GitHub Pages via `actions/deploy-pages`

**One-time repo setting:** `Settings → Pages → Source → GitHub Actions`

### Custom domain DNS

| Type | Name | Value |
|---|---|---|
| `CNAME` | `cv` | `robertovallado.github.io` |

Then: `Settings → Pages → Custom domain → cv.robertovallado.dev` → enable **Enforce HTTPS**.

---

## License

Forked from [lissy93/cv](https://github.com/Lissy93/cv) by Alicia Sykes, MIT licensed. See [`LICENSE`](LICENSE).
