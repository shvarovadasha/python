import sys

filename = sys.argv[1]
vlan_filter = int(input("введите номер vlan: "))
entries = []
with open(filename) as file:
    for line in file:
        parts = line.split()
        if len(parts) == 4 and parts[0].isdigit():
            vlan = int(parts[0])
            mac = parts[1]
            interface = parts[3]
            entries.append((vlan, mac, interface))

n = len(entries)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if entries[j][0] > entries[j + 1][0]:
            entries[j], entries[j + 1] = entries[j + 1], entries[j]

for vlan, mac, interface in entries:
    if vlan == vlan_filter:
        print(f"{vlan:4} {mac} {interface}")