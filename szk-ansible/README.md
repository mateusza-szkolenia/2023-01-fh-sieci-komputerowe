# Ansible

Uruchomienie playboooka:

```
ansible-playbook -i inventory.yaml moj-playbook.yaml
```

Uruchomienie playbooka tylko na określonych serwerach:
* `--limit=grupa1` -- tylko na serwerach z grupy `grupa1`
* `--limit=host1,host2` -- tylko na serwerach `host1` i `host2`
* `--limit='grupa7,!host9'` -- tylko na serwerach z grupy `grupa7`, ale oprócz serwera `host9`

Uruchomienie tylko niektórych zadań z playbooka:
* `--tags=tag111` -- tylko zadania oznaczone tagiem `tag111`
* `--tags=aaa,bbb` -- tylko zadania oznaczone jednym z tagów: `aaa` lub `bbb`

Aby tylko sprawdzić co i gdzie się uruchomi:
* `--list-hosts`
* `--list-tags`

**Uwaga! Przed uruchomieniem trzeba upewnić się, że ansible ma dostęp przez ssh do serwera oraz, że na serwerze jest python3**

```
ssh root@serwer
```

