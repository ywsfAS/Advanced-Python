
adresses_ip = ["192.168.0.1", "10.0.0.1", "172.16.0.1", "200.100.50.1", "169.254.0.1"]


first_address = adresses_ip[0]
print("Première adresse:", first_address)


last_address = adresses_ip[-1]
print("Dernière adresse:", last_address)


third_address = adresses_ip[2]
print("Troisième adresse:", third_address)


adresses_ip.append("172.31.0.1")


adresses_ip.remove("200.100.50.1")

print("Nombre d'adresses restantes:", len(adresses_ip))

IsExist =  "192.168.0.1" in adresses_ip
print("192.168.0.1 est présente?", IsExist)

def ip_class(ip):
    first_octet = int(ip.split('.')[0])
    if 1 <= first_octet <= 126:
        return "Classe A"
    elif 128 <= first_octet <= 191:
        return "Classe B"
    elif 192 <= first_octet <= 223:
        return "Classe C"
    else:
        return "Autre"

print("Classe de 10.0.0.1:", ip_class("10.0.0.1"))

adresses_ip.sort()
print("Adresses triées:", adresses_ip)

class_c_ips = [ip for ip in adresses_ip if ip_class(ip) == "Classe C"]
print("Adresses Classe C:", class_c_ips)

def is_public(ip):
    first, second, *_ = map(int, ip.split('.'))
    # Private IP ranges
    if (first == 10) or (first == 172 and 16 <= second <= 31) or (first == 192 and second == 168):
        return False
    # APIPA
    if first == 169 and second == 254:
        return False
    return True

public_ips_count = sum(is_public(ip) for ip in adresses_ip)
print("Nombre d'adresses publiques:", public_ips_count)
