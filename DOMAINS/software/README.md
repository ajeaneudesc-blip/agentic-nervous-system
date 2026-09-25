# Software — branche de l'Unified Agentic Nervous System

Cette branche n'est PAS un système séparé. Elle constitue le domaine Software / Engineering de l'OS agentique.

## Position dans l'OS

```text
agentic_nervous_system/
├── SYSTEM/
├── REGISTRY/
├── RUNTIME/
├── MEMORY/
├── PROJECTS/
└── DOMAINS/
    ├── commercial/
    ├── creative/
    └── software/        ← cette branche
```

Les 10 agents Software (définitions de rôle sous `agents/`), les guardrails
(`GUARDRAILS.md`), la config budget/permissions et la référence de stack
technique appartiennent au même OS et sont routés depuis les registries et
`SYSTEM/context_map.yaml`.

Le système conserve un seul état global (`RUNTIME/state.json`) et une
seule constitution (`CLAUDE.md` / `SYSTEM/constitution.md`). Les
permissions sont gouvernées à deux niveaux complémentaires :
`SYSTEM/permissions.yaml` (gates humains 0-4, racine, tout le système) et
`DOMAINS/software/config/agent_permissions/permissions.json` (allowlist
d'outils par agent, Software uniquement) — voir les commentaires de ces
deux fichiers pour le détail.

**Exécution** : Claude Code, dans Claude Desktop, lit les définitions de
rôle et exécute directement le travail (code, tests, specs) en appliquant
`GUARDRAILS.md` — il n'y a pas d'orchestrateur séparé (LangGraph a été
retiré) ni de pont d'intégration externe (n8n/Codex).

**Playbooks de référence** : chaque rôle a `agents/<rôle>/playbooks/`
(sous-dossiers `skills/` et `agents/`, + `INDEX.md`), une sélection curée
depuis la bibliothèque ECC (Everything Claude Code) pertinente pour un
studio web/app — le reste (santé, trading, logistique, homelab, vidéo…) a
été écarté comme hors sujet. `DOMAINS/software/playbooks/shared/` contient
les playbooks transverses à tous les rôles. Ce sont des références à
ouvrir à la demande quand une tâche précise le justifie, jamais chargées
par défaut — voir `DOMAINS/software/CLAUDE.md` §11.
