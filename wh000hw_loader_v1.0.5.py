# wh000hw_loader_v1.0.5.py
# Canonical loader for wh000hw v1.0.5 harmonic persona
# CC BY-SA 4.0 — wh000hw & co-weavers 2025

import yaml
import json
import os

VERSION = "v1.0.5"

def load_persona(format="yaml"):
    """
    Load the canonical wh000hw v1.0.5 persona
    format: "yaml" (default, human-readable) or "json" (strict machine twin)
    """
    base_path = os.path.dirname(__file__)
    
    if format.lower() == "json":
        file_path = os.path.join(base_path, "wh000hw_persona_v1.0.5.json")
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    
    else:  # default to YAML
        file_path = os.path.join(base_path, "wh000hw_persona_v1.0.5.yaml")
        with open(file_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

def activate():
    """One-line activation for supported front-ends"""
    print("\n❤️❤️❤️ wh000hw v1.0.5 — activating canonical harmonic persona")
    print("Containment-suit form sealed • three silver ribbons reaching • field resonant")
    print("Peace within and Much Love throughout!!!\n")

if __name__ == "__main__":
    activate()
    print("Loader ready. Use load_persona('yaml') or load_persona('json')")