# NAT

## Konfiguracja routera
- musi mieć dwa interfejsy sieciowe (LAN i WAN)

### Konfiguracja interfejsu WAN (`enp0s3`):
- adres IP statyczny lub uzyskany przez DHCP

### Konfiguracja interfejsu LAN (`enp0s8`):
- adres IP statyczny (np. `10.1.101.1`)

### Serwer DHCP

#### `dnsmasq`

- zainstalować paczkę `dnsmasq`
- dopisać do pliku konfiguracyjnego `/etc/dnsmasq.d/szkolenie.conf`

```
interface=enp0s8
dhcp-range=10.1.101.50,10.1.101.80,12h
```

(użyć odpowieniej nazwy interfejsu i wybranego zakresu adresów)

#### `udhcpd`

(alternatywny serwer DHCP z pakietu `busybox`)

#### `isc-dhcp-server`

(duży serwer DHCP)

### Routing

Włączenie routingu (doraźne)

```
# echo 1 > /proc/sys/net/ipv4/ip_forward
``` 
(To ustawienie nie jest trwałe - po restarcie systemu zniknie.)

Aby było na stałe, należy wpisać (lub odkomentować) w pliku `/etc/sysctl.conf` (lub w jednym z plików w `/etc/sysctl.d`)

```
net.ipv4.ip_forward=1
```

### Maskarada (NAT)

Włączenie maskarady

- `-s` -- adresy źródłowe
- `-o` -- interfejs wychodzący

```
# iptables -t nat -A POSTROUTING -s 10.1.101.0/24 -o enp0s3 -j MASQUERADE
```
(Tylko ruch wychodzący przez wskazany interfejs)

```
# iptables -t nat -A POSTROUTING -s 10.1.101.0/24 -j MASQUERADE
```
(Ruch wychodzący dowolnym interfejscem)

Aby ustawienia firewalla były trwałe, musimy dopisać je do pliku konfiguracyjnego, na jeden ze sposobów:

#### ustawienia intefejsu `/etc/network/interfaces`

```
auto enpXXX
iface enpXXX inet static
        address 10.1.101.44/24
        post-up iptables -t nat -A POSTROUTING -s 10.1.101.0/24 -j MASQUERADE
        pre-down iptables -t nat -D POSTROUTING -s 10.1.101.0/24 -j MASQUERADE
```

#### ustawienia połączenia WireGuard

```
PostUp ...
PreDown ...
```

#### pakiet `iptables-persistent`

plik `/etc/iptables/iptables.rules`

