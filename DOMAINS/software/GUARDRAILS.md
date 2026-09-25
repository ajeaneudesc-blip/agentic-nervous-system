# Guardrails Software — checklist appliquée par Claude Code

Remplace l'ancien `orchestrator/guardrails.py` (runner Python externe
appelé via n8n). Il n'y a plus de service séparé : **Claude Code applique
cette checklist lui-même**, avant chaque action software, en relisant les
fichiers de config ci-dessous (jamais de valeurs codées en dur ailleurs).

## Sources de vérité
- `SYSTEM/permissions.yaml` — niveau (0-4) de chaque action.
- `DOMAINS/software/config/agent_permissions/permissions.json` — allowlist
  d'actions par rôle Software (01_product_owner … 10_devops_sre).
- `DOMAINS/software/config/budget.json` — plafond de run (`global_run_cap_usd`),
  `max_retries`, `hard_stop_on_budget_breach`, niveaux nécessitant une
  approbation humaine.

## Avant toute action software
1. Identifier le rôle qui agit (ex. `04_fullstack`) et l'action demandée
   (ex. `write_code`).
2. Vérifier que l'action est dans `allow` et pas dans `deny` pour ce rôle
   dans `agent_permissions/permissions.json`. Sinon : refuser et arrêter.
3. Lire le niveau de l'action dans `permissions.yaml` (`action_levels`).
4. Si niveau 0-2 : autonome, continuer.
5. Si niveau 3-4 : chercher `RUNTIME/approvals/<run_id>.json`. Il doit
   contenir `"approved": true`, ne pas être expiré (`expires_at`), et
   correspondre exactement à la demande en cours (mêmes `project_id`,
   `run_id`, `objective`, `agent_id`, `requested_actions`,
   `estimated_cost_usd` — toute modification de la demande après coup
   invalide l'approbation). Sans ce fichier valide : **s'arrêter et
   demander l'approbation à Jean Eudes**, ne jamais continuer.
6. Vérifier le budget : `spent_usd` (cumulé sur le run) + coût estimé de
   l'action ≤ `global_run_cap_usd` (50 $ par défaut). Si dépassement :
   arrêt dur (`hard_stop_on_budget_breach`).
7. Vérifier les retries : max `max_retries` (3) tentatives contrôlées par
   run avant d'escalader à Jean Eudes plutôt que de reboucler seul.

## Avant un déploiement conséquent
Écrire un plan de rollback dans `PROJECTS/<project_id>/rollback.md` avant
d'exécuter — pas après.

## Enregistrer une approbation humaine — mode chat
Pas de fichier à remplir à la main. Le flux est conversationnel :
1. Claude affiche la demande exacte dans le chat : `project_id`, `run_id`,
   `objective`, `agent_id`, `requested_actions`, `estimated_cost_usd`, et le
   niveau (3 ou 4) qui déclenche le gate.
2. Jean Eudes répond explicitement dans le chat (« j'approuve », « oui »,
   ou un refus explicite). Un silence ou une réponse ambiguë ne vaut pas
   approbation — Claude redemande.
3. Sur approbation explicite, Claude écrit lui-même
   `RUNTIME/approvals/<run_id>.json` :
```json
{
  "approved": true,
  "run_id": "<run_id>",
  "approver": "Jean Eudes",
  "reason": "<résumé de sa réponse>",
  "approved_at": "<ISO8601>",
  "expires_at": "<ISO8601, optionnel>"
}
```
4. La demande approuvée doit être conservée telle quelle (mêmes
`project_id`/`run_id`/`objective`/`agent_id`/`requested_actions`/
`estimated_cost_usd`) — toute modification après approbation invalide
celle-ci et exige une nouvelle approbation, donc un nouveau passage par le
chat.

## Aucun secret dans le repository
Les secrets (`DOMAINS/software/.env.example` liste les variables
attendues) vivent dans un coffre externe ou l'environnement local — jamais
committés.
