# Architecture d'intégration
Le système nerveux racine est la couche de gouvernance/contextualisation.
`DOMAINS/software` est sa couche de delivery logiciel.

| Couche | Responsabilité |
|---|---|
| CLAUDE.md + SYSTEM | constitution, routing, limites |
| REGISTRY | agents/skills métier |
| PROJECTS | vérité du projet |
| DOMAINS/software | delivery logiciel contrôlé (rôles, guardrails) |
| Claude Code | exécution directe (spec, code, tests, déploiement préparé) |
| Claude Desktop (MCP natif) | accès outils externes (Figma, Supabase, GitHub, etc.) |
| Playwright/Lighthouse/Sentry | preuves qualité et observabilité |

Le pilote métier existant reste `2026-P001-client-acquisition`.
Un pilote software dédié peut ensuite être `2026-P002-image-to-webp`.
