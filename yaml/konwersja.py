#!/usr/bin/env python3

import yaml
import json

PLIK_WEJ = "osoby.yaml"
PLIK_WYJ = "osoby.json"

with open(PLIK_WEJ) as f:
    osoby = yaml.load(f, Loader=yaml.SafeLoader)

with open(PLIK_WYJ, 'w') as f2:
    json.dump(osoby, f2, indent=4)

