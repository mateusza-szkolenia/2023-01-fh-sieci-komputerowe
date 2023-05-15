#!/usr/bin/env python3

import json
import yaml

PLIK_WEJ = "osoby.json"
PLIK_WYJ = "osoby.yaml"

with open(PLIK_WEJ) as f:
    osoby = json.load(f)

with open(PLIK_WYJ, 'w') as f2:
    yaml.dump(osoby, f2, allow_unicode=True)

