# Menedżery pakietów

## `APT` / `dpkg`

Systemy:
- Debian
- Ubuntu
- *i pochodne*

### Polecenia:

- `apt-get update` - aktualizacja listy pakietów
- `apt-get upgrade` - aktualizacja pakietów (programów)

- `dpkg -L xxxxxxx` - lista plików zainstalowanych przez dany pakiet
- `dpkg -S /xxx/yyyy/zzzzz` - jaki pakiet zawiera dany plik

- `dpkg -l` - lista zainstalowanych pakietów
- `dpkg --get-selection` - lista zainstalowanych pakietów (w innym formacie)

- `dpkg -s xxxxxxx` - status i informacje o pakiecie

