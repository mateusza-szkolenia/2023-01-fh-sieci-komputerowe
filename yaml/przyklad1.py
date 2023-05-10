#!/usr/bin/env python3

import yaml

PLIK = "osoby.yaml"
ROK = 2023

with open(PLIK) as f:
    osoby = yaml.load(f, Loader=yaml.SafeLoader)

for osoba in osoby:
    imie = osoba['imie']
    nazw = osoba['nazwisko']
    wiek = ROK - osoba['rok_urodzenia']
    print(f"* {imie} {nazw} ({wiek})")

