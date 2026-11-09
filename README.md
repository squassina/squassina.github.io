# Ricardo Squassina Lee — Personal Website

Personal portfolio and professional profile built with Jekyll and the [al-folio](https://github.com/alshedivat/al-folio) starter/runtime.

## Local development

Requirements: Ruby 3.3+ and Bundler.

```bash
bundle install
bundle exec jekyll serve
```

Open http://localhost:4000.

## Build

```bash
JEKYLL_ENV=production bundle exec jekyll build
```

The generated website is written to `_site/`.

## Languages

- Portuguese (Brazil): `/`
- English: `/en/`

## Deployment

The `feat/al-folio-theme` branch runs a build-only GitHub Actions workflow and uploads the generated site as an artifact. It intentionally does **not** publish to the production GitHub Pages branch. Production remains on `master` until the migration is reviewed and explicitly approved.

## Theme

This site uses the al-folio v1 runtime through the `al_folio_core` and `al_icons` Ruby gems. See the upstream project documentation for setup and customization.
