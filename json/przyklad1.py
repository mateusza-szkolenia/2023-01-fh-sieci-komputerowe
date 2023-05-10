#!/usr/bin/env python3

import json

PLIK = "osoby.json"
ROK = 2023

with open(PLIK) as f:
    osoby = json.load(f)

for osoba in osoby:
    imie = osoba['imie']
    nazw = osoba['nazwisko']
    wiek = ROK - osoba['rok_urodzenia']
    print(f"* {imie} {nazw} ({wiek})")

