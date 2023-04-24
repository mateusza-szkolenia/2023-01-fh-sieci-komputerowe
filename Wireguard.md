# Wireguard

Instalacja wireguarda:
```
# apt-get install -y wireguard
```

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
# aby puścić przez WG cały ruch:
AllowedIPs = 0.0.0.0/0
```

Uruchomić interface:

```
# wg-quick up wg0
```

Wyświetlić klucz publiczny:

```
# wg
interface: wg0
  public key: cVk8sXxkrddQkgJcN0FWUQF62jllNQAI+rnrSpjzlTI=
  private key: (hidden)
  listening port: 54385

peer: 3Y+TsOJmXijSA42XLI1vbyFAAz9xBZPBz1QDrqEzTiQ=
  endpoint: 164.92.187.104:51820
  allowed ips: 10.77.0.0/24
```

