# CV Web App

Interactive SvelteKit site for Roberto's CV. All data is loaded **server-side from the local filesystem** (`resume.yml` at the project root) — no GitHub fetch needed, changes appear immediately in `npm run dev`.

Live at [cv.robertovallado.dev](https://cv.robertovallado.dev) — deployed automatically on push to `main`.

---

## Quick start

```bash
npm install
npm run dev        # http://localhost:5173
npm run build      # production build (GITHUB_PAGES=true for static adapter)
npm run preview    # preview production build
```

---

## Where content comes from

The app has two content sources that work together:

### `resume.yml` (project root)
Read at build/dev time via `+page.server.ts` and `+layout.server.ts`. Powers:
- **Sidebar** — name, headline, social links (`basics`)
- **Home page** — full resume summary (all sections)
- **Experience page** — job entries, using `highlights-fr` when locale is FR
- **Skills page** — skill groups and keywords
- **PDF downloads** — both EN and FR PDFs are generated from this file

### `src/lib/locales/en.json` + `fr.json`
Static i18n files for all narrative and UI content. Powers:
- **Intro page** — full bio paragraphs
- **Achievements page** — stats and awards list
- **Contact page** — all text
- **Ideal Role page** — values, requirements, intro text
- **All nav labels, buttons, section headers** — every UI string

Switch language with the **EN / FR** toggle in the top-right header. The active locale is saved to `localStorage`.

---

## Structure

```
src/
  lib/
    i18n.ts              Custom locale store — $t('key'), setLocale('fr')
    locales/en.json      English strings and content
    locales/fr.json      French translations
  routes/
    +layout.server.ts    Reads resume.yml → basics for sidebar
    +layout.svelte       Sidebar, nav, EN/FR toggle
    +page.server.ts      Reads resume.yml → home page data
    +page.svelte         Home — summary of all CV sections
    intro/               Bio (i18n JSON)
    experience/          Jobs from resume.yml, locale-aware highlights
    skills/              Skills from resume.yml + Language badges
    achievements/        Stats + awards (i18n JSON)
    contact/             Contact info (i18n JSON)
    ideal-role/          Role preferences (i18n JSON)
    download/            Triggers PDF download (EN or FR based on locale)
  components/
    Language.svelte      Tech badge component (SimpleIcons)
  styles/                SCSS — forest green dark theme
svelte.config.js         Static adapter, base path '' for custom domain
```

See the [root README](../README.md) for the full PDF pipeline, CI/CD, and deployment docs.
