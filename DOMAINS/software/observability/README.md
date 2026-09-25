# Observability
Chaque run doit conserver au minimum : run_id, project_id, agent, action,
status, duration, estimated/spent cost, approval state, evidence/artifact paths,
error/retry count — écrits dans `PROJECTS/<project_id>/RUNS/`. Une connexion
Sentry peut être ajoutée sans modifier les règles de permission.
