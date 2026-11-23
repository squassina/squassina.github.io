# Domain Docs

How engineering skills should consume this repository's domain documentation.

## Before exploring

- Read `GLOSSARY.md` at the repository root if it exists.
- Read `GLOSSARY-MAP.md` at the repository root if it exists.
- Read relevant ADRs in `docs/adr/`.

Use relevant domain documentation only. Do not create glossary or ADR files before a real term or trade-off has been resolved.

## File structure

Single-context repository:

```text
/
├── GLOSSARY.md
└── docs/adr/
```

## Use glossary vocabulary

When output names a domain concept, use the term defined in `GLOSSARY.md`.

If a concept is not in the glossary, signal the gap instead of silently inventing equivalent terminology.

## Flag ADR conflicts

If output contradicts an existing ADR, surface the conflict explicitly rather than silently overriding it.
