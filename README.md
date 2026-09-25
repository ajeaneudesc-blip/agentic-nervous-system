# Unified Agentic Nervous System — Phase 0 (pilote)

Squelette correspondant à la **Phase 0** du guide d'implémentation v2
(section 4.1) — le strict nécessaire pour faire tourner le projet pilote
`2026-P001-client-acquisition` avant d'étendre vers la Phase 1 complète.

Environnement d'exécution unique : **Claude Desktop** (Cowork, Claude Code,
Claude Design). Plus de pont externe (Codex, n8n) — Claude Code lit ce
dossier et exécute directement.

## Démarrage

1. Ouvrir ce dossier dans Claude Desktop (Cowork ou Claude Code).
2. Claude lit `CLAUDE.md` puis `RUNTIME/state.json` — jamais tout le
   reste par défaut.
3. Donner un objectif, pas un agent : le routing se fait via
   `SYSTEM/context_map.yaml` + `REGISTRY/`.

## Ce qui est déjà en place

- `CLAUDE.md` — constitution racine, sous ~2000 tokens.
- `SYSTEM/context_map.yaml` — routes déclarées, avec un budget indicatif
  (12 fichiers / 6000 tokens max) que Claude applique lui-même — plus de
  script de validation dédié.
- `REGISTRY/agents.json` + `skills.json` — registries générés depuis les sources sous `DOMAINS/*`.
  **Ne jamais éditer ces fichiers à la main** : ils sont régénérés depuis
  `DOMAINS/*/agents/*.yaml` et `DOMAINS/*/skills/*.yaml` via
  `scripts/build_registry.py`.
- `DOMAINS/commercial/`, `DOMAINS/creative/` et `DOMAINS/software/` — agents, skills, playbooks,
  données de départ.
- `RUNTIME/` — état courant, file d'attente du jour (exemple pré-rempli
  pour `DAILY-COMMERCIAL`), logs.
- `PROJECTS/2026-P001-client-acquisition/` — le projet pilote.
- `MEMORY/` — durable + épisodique (rotation hebdomadaire à mettre en
  place via un rappel programmé Claude, section 8.5 du guide).
- `scripts/build_registry.py` — régénère les registries depuis les sources.

## Ce qui n'est pas encore construit (volontairement)

Kubernetes, event bus formalisé au-delà d'un JSONL, framework
d'evals complet, les 6 domaines et 67 agents/36 skills complets — tout ça
attend que le pilote ait tourné une fois de bout en bout (section 23 du
guide). Voir le guide d'implémentation complet v2 pour la Phase 1.

## Branche Software
`DOMAINS/software/` est la couche d'exécution Software / Engineering de l'OS :
10 rôles spécialisés, guardrails, budget, approvals, rollback, registre des
repositories de référence. Le système nerveux conserve le contexte et la
gouvernance ; **Claude Code exécute directement**, sans orchestrateur ni
pont d'intégration externe.

Le domaine Commercial qualifie les besoins et prépare les handoffs vers
Creative ou Software. L'exécution ne commence qu'après accord client et
création d'un brief de projet traçable.
