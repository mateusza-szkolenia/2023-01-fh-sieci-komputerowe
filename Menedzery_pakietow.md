# Menedżery pakietów

## `APT` / `dpkg`

Systemy:
- Debian
- Ubuntu
- *i pochodne*

### Polecenia:

- `apt-get update` - aktualizacja listy pakietów
- `apt-get upgrade` - aktualizacja pakietów (programów)
- `apt-get dist-upgrade` - aktualizacja pakietów, również implikująca instalację nowych lub usunięcie obecnych

- `dpkg -L xxxxxxx` - lista plików zainstalowanych przez dany pakiet
- `dpkg -S /xxx/yyyy/zzzzz` - jaki pakiet zawiera dany plik

- `dpkg -l` - lista zainstalowanych pakietów
- `dpkg --get-selection` - lista zainstalowanych pakietów (w innym formacie)

- `dpkg -s xxxxxxx` - status i informacje o pakiecie

### Aktualizacja systemu do nowego wydania

Zmienić w pliku `/etc/apt/sources.list` wszystkie wystąpienia nazwy wydania, np. `bullseye` (Debian 11) na `bookworm` (Debian 12); lub w Ubuntu `jammy` (Ubuntu 22.04 LTS) na `kinetic` (Ubuntu 22.10).

Polecenie w vimie: [ESC] `:%s/bullseye/bookworm/`

Potem:
```
# apt-get update
# apt-get dist-upgrade
```

#### Uwaga odnośnie aktualizacji Ubuntu:

- albo z LTS na kolejny LTS (np. 20.04 LTS do 22.04 LTS)
- albo tylko kolejne wydania: (np. 22.04 LTS na 22.10, potem 22.10 na 23.04 itd.)


