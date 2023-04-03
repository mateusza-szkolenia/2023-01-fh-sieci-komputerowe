# Wireguard

Konfiguracja połączenia VPN z serwerem szkoleniowym:

Na swojej wirtualnej maszynie wygenerować klucz prywatny:

```
# wg genkey
ryewurtewityriutyewurtywutyeurtyiw....
```

Stworzyć plik konfiguracyjny wireguarda, np. `/etc/wireguard/wg0.conf`

```
[Interface]
Address = 10.77.0.XXX
PrivateKey = ryewurtewityriutyewurtywutyeurtyiw...

[Peer]
PublicKey = 3Y+TsOJmXijSA42XLI1vbyFAAz9xBZPBz1QDrqEzTiQ=
Endpoint = szkolenie02.alx.net.pl:51820
AllowedIPs = 10.77.0.0/24
```

