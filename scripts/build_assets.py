#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
ASSETS = ROOT / "assets"

TEMPLATE = (SRC / "template.svg").read_text(encoding="utf-8")

ASSETS.mkdir(parents=True, exist_ok=True)

for scene_path in sorted((SRC / "scenes").glob("*.json")):
    scene = json.loads(scene_path.read_text(encoding="utf-8"))

    name = scene["name"]
    defs_path = SRC / "defs" / scene["defs"]
    body_path = SRC / "bodies" / scene["body"]

    defs = defs_path.read_text(encoding="utf-8").rstrip()
    body = body_path.read_text(encoding="utf-8").rstrip()

    output = TEMPLATE
    output = output.replace("{{ARIA}}", scene["aria"])
    output = output.replace("{{WIDTH}}", str(scene.get("width", 800)))
    output = output.replace("{{HEIGHT}}", str(scene.get("height", 300)))
    output = output.replace("{{VIEWBOX}}", scene.get("viewBox", "0 0 800 300"))
    output = output.replace("{{DEFS}}", defs)
    output = output.replace("{{BODY}}", body)

    (ASSETS / f"{name}.svg").write_text(output + "\n", encoding="utf-8")

print("Generated SVGs:", ", ".join(sorted(p.name for p in ASSETS.glob("*.svg"))))
