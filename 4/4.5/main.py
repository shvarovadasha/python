def get_int_vlan_map(filename):
    access_ports = {}
    trunk_ports = {}

    with open(filename, 'r') as file:
        current_interface = ''
        for line in file:
            line = line.strip()

            if line.startswith('interface'):
                current_interface = line.split()[-1]

            elif line.startswith('switchport access vlan'):
                vlan = int(line.split()[-1])
                access_ports[current_interface] = vlan

            elif line.startswith('switchport trunk allowed vlan'):
                vlans = list(map(int, line.split()[-1].split(',')))
                trunk_ports[current_interface] = vlans

    return access_ports, trunk_ports

access_dict, trunk_dict = get_int_vlan_map('config_sw1.txt')

print('Access-порты:')
for port, vlan in access_dict.items():
    print(f'{port}: VLAN {vlan}')

print('\nTrunk-порты:')
for port, vlans in trunk_dict.items():
    print(f'{port}: VLANs {vlans}')
