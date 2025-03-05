import sys

filename = sys.argv[1]
with open(filename) as file:
    for line in file:
        parts = line.split()
        if len(parts) == 4 and parts[0].isdigit():
            vlan, mac, _, interface = parts
            print(f"{vlan:4} {mac} {interface}")
