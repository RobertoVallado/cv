# CV Web App

Interactive SvelteKit site for the CV. Reads data from [`resume.yml`](../resume.yml) (fetched from GitHub at build time) and renders it as a multi-page site.

Live at [cv.robertovallado.dev](https://cv.robertovallado.dev) — deployed automatically on push to `main`.

## Quick start

```bash
npm install
npm run dev        # http://localhost:5173
npm run build      # production build (set GITHUB_PAGES=true for Pages output)
npm run preview    # preview production build
```

## Structure

- `src/routes/` — page routes (intro, experience, skills, achievements, contact, ideal-role)
- `src/styles/` — SCSS variables and shared styles
- `svelte.config.js` — static adapter config for GitHub Pages

See the [root README](../README.md) for full repo docs and deployment instructions.
