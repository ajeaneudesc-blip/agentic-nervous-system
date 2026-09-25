# Playbook — DAILY-COMMERCIAL

Objectif : identifier ce qui peut encaisser aujourd'hui et préparer les
actions correspondantes, sans charger de contexte créatif ou motion.

## Étapes
1. Lire `DOMAINS/commercial/data/pipeline.csv` et `crm.csv`.
2. Scorer les opportunités ouvertes (probabilité x montant x fraîcheur).
3. Générer au maximum 7 actions priorisées.
4. Pour chaque opportunité qualifiée, recommander l'offre et le domaine de
   delivery (`creative` ou `software`) avec le skill `solution_qualification`.
5. Préparer les brouillons d'outreach (skill `outreach`) pour les actions
   qui en nécessitent.
6. Respecter la politique d'approbation sortante (gate niveau 3 si premier
   contact sur un nouveau canal).
7. Après accord client, préparer un handoff traçable vers le projet Creative
   ou Software concerné ; ne pas démarrer l'exécution sans brief de projet.
8. Mettre à jour `crm.csv`, `pipeline.csv` et le journal de session.
9. Retourner uniquement : blocages, décisions à prendre par Jean Eudes,
   résultats complétés.

## Ne jamais faire
- Charger `DOMAINS/creative/`.
- Ouvrir `LEGACY/`.
- Envoyer un message sans passer par le gate si le canal est nouveau.
