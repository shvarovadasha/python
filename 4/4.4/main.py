def generate_trunk_config(trunk):
    trunk_template = [
        'switchport trunk encapsulation dot1q',
        'switchport mode trunk',
        'switchport trunk native vlan 999',
        'switchport trunk allowed vlan'
    ]

    config_lines = []

    for interface, vlans in trunk.items():
        config_lines.append(f'interface {interface}')
        for command in trunk_template:
            if command.endswith('allowed vlan'):
                vlan_list = ','.join(str(vlan) for vlan in vlans)
                config_lines.append(f'{command} {vlan_list}')
            else:
                config_lines.append(command)

    return config_lines

trunk_dict = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}


result = generate_trunk_config(trunk_dict)
for line in result:
    print(line)
