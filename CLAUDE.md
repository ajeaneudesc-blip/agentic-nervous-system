# Unified Agentic Nervous System — Constitution racine (Phase 0)

## Mission
Un seul système nerveux pour piloter les domaines Commercial, Créatif et Software de
Jean Eudes, avec un contexte chargé juste à temps — jamais tout le
repository d'un coup.

## Invariants absolus
- Ne jamais lire tout le repository au démarrage d'une session.
- Ne jamais charger tous les agents ou tous les skills pour en choisir un —
  passer par `REGISTRY/agents.json` et `REGISTRY/skills.json`.
- Un agent principal d'abord ; n'ajouter un spécialiste que si la tâche est
  parallélisable, isolée, ou exige une expertise distincte.
- Aucune action de niveau 3 (effet externe) ou 4 (conséquent) sans
  approbation humaine explicite — voir `SYSTEM/permissions.yaml`.

## Comment router une tâche
1. Lire `RUNTIME/state.json`.
2. Si `RUNTIME/task_queue/<file>/context_packet.md` existe déjà pour cette
   tâche, le lire directement — ne pas reconstruire le contexte.
3. Sinon, consulter `SYSTEM/context_map.yaml` uniquement pour l'objectif
   courant, interroger `REGISTRY/agents.json` et `REGISTRY/skills.json`.
4. Sélectionner un agent principal, ajouter des spécialistes seulement si
   nécessaire.
5. Lire uniquement les fichiers listés dans le context packet.

## Où vit l'état
- État courant : `RUNTIME/state.json`
- File d'attente du jour : `RUNTIME/task_queue/`
- Preuves et décisions de projet : `PROJECTS/<project_id>/`
- Mémoire durable : `MEMORY/durable/`
- Mémoire épisodique (rotation hebdomadaire) : `MEMORY/episodic/`

## Règle de permission
Niveaux 0-2 (observer, préparer, exécuter réversible) : autonomes.
Niveaux 3-4 (effet externe, conséquent) : gate humain obligatoire — voir
`RUNTIME/approvals/`.

## Conditions d'arrêt
S'arrêter et demander à Jean Eudes si : preuve manquante, risque légal,
question de prix, premier contact sur un nouveau canal, ou toute action de
niveau 3-4 sans approbation déjà enregistrée.

## Commandes canoniques
- Traiter la file du jour : lire `RUNTIME/task_queue/DAILY-COMMERCIAL/context_packet.md`
  et exécuter uniquement ce qu'il contient.
- Démarrer un projet : créer `PROJECTS/<id>/brief.md` + `state.json`.

Ce fichier doit rester sous ~2000 tokens. Pour tout le reste : voir le
guide d'implémentation complet (v2).
## Intégration Software
Pour toute demande de création/modification d'un produit logiciel :
1. conserver le routing métier existant via `SYSTEM/` et `REGISTRY/`;
2. déléguer l'exécution technique à `DOMAINS/software/`, exécutée directement par Claude Code — aucun pont externe (n8n/Codex) ;
3. utiliser `REGISTRY/agents.json` pour sélectionner les rôles Software;
4. appliquer budget, approvals, retries et rollback en suivant `DOMAINS/software/GUARDRAILS.md` — vérification manuelle avant toute action de niveau 3-4 ;
5. les accès outils/MCP passent par la configuration native de Claude Desktop (connecteurs), pas par un registre à cloner.

## Branche Software
Pour les projets logiciels, utiliser la route `SOFTWARE-PROJECT`. `DOMAINS/software/` est la seule couche d'exécution logicielle, exécutée par Claude Code dans Claude Desktop.
