# Software — règles d'exécution
1. Lire d'abord le `CLAUDE.md` racine puis le contexte de la tâche.
2. Ne jamais explorer tout le repository pour choisir un agent.
3. Pour un projet logiciel, utiliser `REGISTRY/agents.json` et les définitions
   sous `DOMAINS/software/agents/`.
4. Ne jamais contourner `DOMAINS/software/GUARDRAILS.md` — appliquer la
   checklist avant chaque action (permissions, budget, approbations, retries).
5. Les actions de niveau 3 ou 4 nécessitent une approbation humaine
   enregistrée dans `RUNTIME/approvals/`.
6. Aucun secret ne doit être écrit dans le repository.
7. Un échec peut déclencher au maximum 3 retries contrôlés.
8. Avant un déploiement conséquent, produire un rollback plan dans
   `PROJECTS/<project_id>/rollback.md`.
9. Claude Code exécute directement le travail logiciel — pas d'orchestrateur
   ni de pont d'intégration externe (n8n/Codex).
10. Les MCP non explicitement configurés dans Claude Desktop sont indisponibles ;
    `DOMAINS/software/config/repos.json` reste une référence de stack technique,
    pas un registre à cloner.
11. Chaque rôle a un dossier `DOMAINS/software/agents/<rôle>/playbooks/`
    (skills + agents de référence, curés depuis ECC — Everything Claude Code)
    listé dans `playbooks:` de son `agent.yaml` et son `INDEX.md`. Ce sont des
    fichiers à lire À LA DEMANDE, seulement quand la tâche touche exactement
    ce sujet (ex. `04_fullstack` ouvre `playbooks/skills/django-patterns/`
    uniquement pour une tâche Django) — jamais chargés par défaut, jamais
    tous ensemble : ça violerait l'invariant de contexte juste-à-temps.
    `DOMAINS/software/playbooks/shared/` contient les playbooks transverses
    (recherche, doc, onboarding codebase), même règle.
