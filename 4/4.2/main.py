def generate_access_config(access, psecurity=False):
    """
    access - словарь access-портов, вида:
        { 'FastEthernet0/12': 10, 'FastEthernet0/14': 11, ... }

    psecurity - контролирует, нужна ли настройка Port Security.
        True  -> добавить настройки безопасности
        False -> не добавлять

    Возвращает список строк конфигурации для всех портов.
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

    result = []

    for interface, vlan in access.items():
        result.append(f'interface {interface}')
        for command in access_template:
            if command.endswith('vlan'):
                result.append(f'{command} {vlan}')
            else:
                result.append(command)

        if psecurity:
            result.extend(port_security)

    return result

access_dict = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17,
    'FastEthernet0/17': 150
}

print("\n--- Конфигурация без Port Security ---")
config_no_sec = generate_access_config(access_dict)
for line in config_no_sec:
    print(line)

print("\n--- Конфигурация с Port Security ---")
config_with_sec = generate_access_config(access_dict, psecurity=True)
for line in config_with_sec:
    print(line)

