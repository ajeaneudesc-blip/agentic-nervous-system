# Prochaines étapes
1. Configurer les MCP nécessaires (Figma, Supabase, GitHub, Stripe, Sentry…)
   directement dans les paramètres de Claude Desktop — plus de registre à cloner.
2. Configurer les secrets listés dans `DOMAINS/software/.env.example` dans un
   coffre externe ou l'environnement local — jamais dans le repository.
3. Donner du contenu réel aux 10 rôles sous `DOMAINS/software/agents/*/agent.yaml`
   (actuellement des squelettes quasi vides) : inputs, outputs, skills, tools.
4. Choisir et lancer un premier pilote software dédié (ex.
   `2026-P002-image-to-webp`) : `PROJECTS/<id>/brief.md` + `state.json`.
5. Tester la checklist `GUARDRAILS.md` sur ce pilote : un run niveau 0-2 de
   bout en bout, puis une action niveau 3-4 avec approbation enregistrée
   dans `RUNTIME/approvals/`.
6. Vérifier qu'un rollback plan est bien produit avant tout déploiement
   conséquent (`PROJECTS/<project_id>/rollback.md`).
