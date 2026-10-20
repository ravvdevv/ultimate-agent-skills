# Upstream projects and integration notes

This repository keeps its own portable workflows and links to specialist projects instead of silently copying entire external toolchains. Check each upstream repository for current setup instructions and license terms before installing, vendoring, or redistributing files.

## Recommended references

| Project | Use it for | Integration decision |
| --- | --- | --- |
| [Superpowers](https://github.com/obra/superpowers) | End-to-end development flow: brainstorming, plans, TDD, code review, and completion verification | Adopt the useful workflow patterns in our portable skills. Use Superpowers itself when its plugin integrations, hooks, and full workflow enforcement are wanted; this repository does not bundle those runtime features. |
| [Anthropic Skills](https://github.com/anthropics/skills) | Official examples, reusable task-specific skills, and the Agent Skills format | Use as a reference for skill structure and focused task instructions. Do not imply this repository is official or copy upstream skill content without preserving license and attribution. |
| [Vercel Skills CLI](https://github.com/vercel-labs/skills) | Cross-agent discovery, installation, selection, and updates | Recommended installer for this repository: `npx skills add ravvdevv/ultimate-agent-skills`. The CLI is external software and is not bundled here; check its current documentation for supported agents and flags. |
| [Matt Pocock's Skills](https://github.com/mattpocock/skills) | Targeted engineering workflows and recurring coding-agent failure modes | Use as a reference for focused skills, explicit decision gates, and review against both spec and repository standards. Our skills are independently written; no upstream files are vendored. |
| [Humanizer](https://github.com/blader/humanizer) | Editing generic or AI-sounding prose without changing meaning | This repository has an independently written, concise `humanizer` workflow. Preserve upstream notices if copying any upstream material. |
| [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Searchable design-system guidance, UI styles, palettes, typography, and platform-specific patterns | Link to and install/use upstream tooling when needed. This repository does not include its data assets or CLI. Check the upstream LICENSE before redistribution. |
| [Impeccable](https://github.com/pbakaus/impeccable) | Design critique, polish, accessibility/performance audits, and visual iteration | Use the upstream installer for its full commands and detector rules. This repository's `frontend-design-review` is a portable checklist, not a copy of Impeccable. Check the upstream LICENSE before redistribution. |
| [gstack](https://github.com/garrytan/gstack) | Product planning, design/engineering review, QA, debugging, and shipping workflows | The `product-planning` and `qa-release` skills are independent, runtime-agnostic adaptations of general workflow ideas. They do not include gstack scripts, browser tooling, telemetry, or command router. Check upstream setup and license before installing or copying files. |
| [Everything Claude Code (ECC)](https://github.com/affaan-m/ecc) | Broader engineering skills, specialist agents, hooks, and automation | Treat as a reference library. Cherry-pick only a specific workflow after inspecting its files, dependencies, license, and overlap with existing skills. No ECC agents or hooks are bundled here. |

## What we adopt

- **Reliable workflow:** clarify the goal, plan proportionally, test meaningful behavior, review changes, and verify completion with fresh evidence.
- **Low-friction installation:** use the community skills CLI when supported instead of maintaining a custom installer for every agent.
- **Focused skills:** keep each skill small and triggerable, with a clear description, workflow, guardrails, and completion checklist.
- **Discoverability:** organize skills by job and let users install only what they need.
- **Honest capabilities:** distinguish portable instructions from hooks, plugins, subagents, browser tools, and other runtime-specific features.

## Behavior skills kept separate

Caveman Ultra, Ponytail Ultra, and i-have-adhd are user-selected behavior skills. Keep their actual upstream files and host-specific startup configuration in the environment where they are installed; this repository does not claim to bundle or automatically activate those third-party skills. The local `attention-friendly` skill provides a small, generic workflow alternative.

## Attribution and licensing

- Do not remove upstream copyright or license notices from copied files.
- Record the exact source URL, version or commit, license, and local modifications for any future vendored skill.
- A link to a project is not a substitute for checking its license.
- Prefer original workflow summaries when the full upstream runtime is not required.
