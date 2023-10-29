# SSH

## Generowanie kluczy (Windows 10, linia poleceń)


```command
C:\> ssh-keygen -t ed25519
```

Klucz jest zapisany do pliku `.ssh/id_ed25519.pub` i należy go wrzucić na serwer do pliku: `.ssh/authorized_keys`

## Kopiowanie plików między komputerami:


### Na serwer

```command
C:\> scp jakis-plik.png nazwa.konta@serwer:
```

### Z serwera
```command
C:\> scp nazwa@serwer:plik.jpg ./
```

