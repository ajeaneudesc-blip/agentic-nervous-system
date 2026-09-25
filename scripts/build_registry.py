#!/usr/bin/env python3
"""
Régénère REGISTRY/agents.json et REGISTRY/skills.json depuis les fichiers
source DOMAINS/*/agents/*.yaml et DOMAINS/*/skills/*.yaml.

Ne jamais éditer les fichiers REGISTRY/*.json à la main — les fichiers
YAML sous DOMAINS/ sont la seule source de vérité (guide v2, section 4,
étape 4).

Usage:
    python scripts/build_registry.py
"""
import json
from pathlib import Path

try:
    import yaml
except ImportError:
    raise SystemExit("Ce script requiert PyYAML : pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
ENCODING = "utf-8"  # forcé explicitement : sur Windows, l'encodage par
# défaut de open()/write_text() est celui de la console (souvent cp1252),
# pas UTF-8 — sans ça, le script peut planter ou corrompre du texte dès
# qu'un fichier source contient un caractère hors cp1252.


def check_unique_ids(entries: list, kind: str) -> None:
    seen = {}
    for e in entries:
        eid = e.get("id")
        if eid in seen:
            raise SystemExit(
                f"ID {kind} dupliqué : '{eid}' défini dans "
                f"{seen[eid]} et {e['source_path']}."
            )
        seen[eid] = e["source_path"]


def collect(pattern: str) -> list:
    entries = []
    for path in sorted(ROOT.glob(pattern)):
        with path.open(encoding=ENCODING) as f:
            data = yaml.safe_load(f)
        data["source_path"] = str(path.relative_to(ROOT))
        data.setdefault("inputs", [])
        data.setdefault("outputs", [])
        data.setdefault("skills", [])
        data.setdefault("tools", [])
        data.setdefault("requires_human", False)
        data.setdefault("requires_human_for", [])
        entries.append(data)
    return entries


def collect_agents() -> list:
    entries = []
    for path in sorted((ROOT / "DOMAINS").glob("*/agents/**/*.yaml")):
        with path.open(encoding=ENCODING) as f:
            data = yaml.safe_load(f)
        data.setdefault("domain", path.relative_to(ROOT).parts[1])
        data.setdefault("inputs", [])
        data.setdefault("outputs", [])
        data.setdefault("skills", [])
        data.setdefault("tools", [])
        data.setdefault("requires_human", False)
        data.setdefault("requires_human_for", [])
        data["source_path"] = str(path.relative_to(ROOT))
        entries.append(data)
    return entries


def main():
    agents = collect_agents()
    skills = collect("DOMAINS/*/skills/*.yaml")
    check_unique_ids(agents, "agent")
    check_unique_ids(skills, "skill")

    agents_out = {
        "_comment": "Régénéré par scripts/build_registry.py depuis DOMAINS/*/agents/*.yaml — ne jamais éditer à la main.",
        "agents": agents,
    }
    skills_out = {
        "_comment": "Régénéré par scripts/build_registry.py depuis DOMAINS/*/skills/*.yaml — ne jamais éditer à la main.",
        "skills": [
            {
                "id": s["id"],
                "domain": s["domain"],
                "when_to_use": s.get("when_to_use", []),
                "source_path": s["source_path"],
            }
            for s in skills
        ],
    }

    (ROOT / "REGISTRY" / "agents.json").write_text(
        json.dumps(agents_out, indent=2, ensure_ascii=False) + "\n",
        encoding=ENCODING,
    )
    (ROOT / "REGISTRY" / "skills.json").write_text(
        json.dumps(skills_out, indent=2, ensure_ascii=False) + "\n",
        encoding=ENCODING,
    )
    print(f"{len(agents)} agents, {len(skills)} skills régénérés dans REGISTRY/")


if __name__ == "__main__":
    main()
