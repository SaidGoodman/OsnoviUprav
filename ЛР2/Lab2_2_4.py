def network_addresses(ip, mask):
    ip_parts = ip.split(".")
    mask_parts = mask.split(".")
    network = []
    broadcast = []
    for i in range(4):
        ip_num = int(ip_parts[i])
        mask_num = int(mask_parts[i])
        network.append(str(ip_num & mask_num))
        broadcast.append(str(ip_num | (255 - mask_num)))
    return ".".join(network), ".".join(broadcast)

ip_address = input("Введите ip-адрес: ")
net_mask = input("Введите маску сети: ")
network_address, broadcast_address = network_addresses(ip_address, net_mask)

print("Адрес сети: ", network_address)
print("Широковещательный адрес: ", broadcast_address)
