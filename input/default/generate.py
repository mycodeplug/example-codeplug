#!/usr/bin/env python3

# This generates the same codeplug as generate.sh
# using python code.

from pathlib import Path
import os

from dzcb.recipe import CodeplugRecipe

cp_dir = Path(__file__).parent
output = Path(os.environ.get("OUTPUT") or (cp_dir / ".." / ".." / "OUTPUT"))

CodeplugRecipe(
    source_pnwdigital=True,
    source_seattledmr=True,
    source_default_k7abd=True,
    source_k7abd=[(cp_dir / "k7abd")],
    source_repeaterbook_proximity=cp_dir / "prox.csv",
    repeaterbook_states=["washington", "oregon"],
    repeaterbook_name_format='{Callsign} {Nearest City} {Landmark}',
    scanlists_json=cp_dir / "scanlists.json",
    exclude=cp_dir / "exclude.csv",
    order=cp_dir / "order.csv",
    replacements=cp_dir / "replacements.csv",
    output_anytone=True,
    output_dmrconfig=[(cp_dir / "example-d878uv.conf")],
    output_farnsworth=[(cp_dir / "example-md-uv380.json")],
    output_gb3gf=True
).generate(output / cp_dir.name)
