def generate_access_config(access, psecurity=False):
    """
    access - словарь access-портов, вида:
        { 'FastEthernet0/12': 10, ... }

    psecurity - если True, добавить port-security команды

    Возвращает словарь:
        ключ: имя интерфейса
        значение: список конфигурационных строк
    """
    access_template = [
        'switchport mode access',
        'switchport access vlan',
        'switchport nonegotiate',
        'spanning-tree portfast',
        'spanning-tree bpduguard enable'
    ]

    port_security = [
        'switchport port-security maximum 2',
        'switchport port-security violation restrict',
        'switchport port-security'
    ]

    config_dict = {}

    for interface, vlan in access.items():
        commands = []
        for command in access_template:
            if command.endswith('vlan'):
                commands.append(f'{command} {vlan}')
            else:
                commands.append(command)

        if psecurity:
            commands.extend(port_security)

        config_dict[interface] = commands

    return config_dict

access_dict = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17,
    'FastEthernet0/17': 150
}

print("\n--- Конфигурация без Port Security ---")
config_no_sec = generate_access_config(access_dict)
for intf, cmds in config_no_sec.items():
    print(f'\ninterface {intf}')
    for cmd in cmds:
        print(cmd)

print("\n--- Конфигурация с Port Security ---")
config_with_sec = generate_access_config(access_dict, psecurity=True)
for intf, cmds in config_with_sec.items():
    print(f'\ninterface {intf}')
    for cmd in cmds:
        print(cmd)
