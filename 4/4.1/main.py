def generate_access_config(access):

    access_template = [
        'switchport mode access',
        'switchport access vlan',
        'switchport nonegotiate',
        'spanning-tree portfast',
        'spanning-tree bpduguard enable'
    ]

    result = []

    for interface, vlan in access.items():
        result.append(f'interface {interface}')
        for command in access_template:
            if command.endswith('vlan'):
                result.append(f'{command} {vlan}')
            else:
                result.append(command)

    return result

access_dict = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17,
    'FastEthernet0/17': 150
}

config = generate_access_config(access_dict)
for line in config:
    print(line)
