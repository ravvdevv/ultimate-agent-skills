# Upstream projects and integration notes

This repository keeps its own portable workflows and links to specialist projects instead of silently copying entire external toolchains. Check each upstream repository for current setup instructions and license terms before installing, vendoring, or redistributing files.

## Recommended references

| Project | Use it for | Integration decision |
| --- | --- | --- |
| [Humanizer](https://github.com/blader/humanizer) | Editing generic or AI-sounding prose without changing meaning | This repository has an independently written, concise `humanizer` workflow. The upstream project is MIT-licensed; preserve its notice if copying any upstream material. |
| [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Searchable design-system guidance, UI styles, palettes, typography, and platform-specific patterns | Link to and install/use upstream tooling when needed. Do not pretend this repository includes its data assets or CLI. Check the upstream LICENSE before redistribution. |
| [Impeccable](https://github.com/pbakaus/impeccable) | Design critique, polish, accessibility/performance audits, and visual iteration | Use the upstream installer for its full commands and detector rules. This repository's `frontend-design-review` is a portable checklist, not a copy of Impeccable. Check the upstream LICENSE before redistribution. |
| [gstack](https://github.com/garrytan/gstack) | Product planning, design/engineering review, QA, debugging, and shipping workflows | The `product-planning` and `qa-release` skills are independent, runtime-agnostic adaptations of general workflow ideas. They do not include gstack scripts, browser tooling, telemetry, or command router. Check upstream setup and license before installing or copying files. |
| [Everything Claude Code (ECC)](https://github.com/affaan-m/ecc) | Broader engineering skills, specialist agents, hooks, and automation | Treat as a reference library. Cherry-pick only a specific workflow after inspecting its files, dependencies, license, and overlap with existing skills. No ECC agents or hooks are bundled here. |

## Behavior skills kept separate

Caveman Ultra, Ponytail Ultra, and i-have-adhd are user-selected behavior skills. Keep their actual upstream files and host-specific startup configuration in the environment where they are installed; this repository does not claim to bundle or automatically activate those third-party skills. The local `attention-friendly` skill provides a small, generic workflow alternative.

## Attribution and licensing

- Do not remove upstream copyright or license notices from copied files.
- Record the exact source URL, version or commit, license, and local modifications for any future vendored skill.
- A link to a project is not a substitute for checking its license.
- Prefer original workflow summaries when the full upstream runtime is not required.
