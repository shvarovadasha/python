def ignore_command(command, ignore):
    """
    Функция проверяет, содержится ли в команде слово из списка ignore.
    command - строка. Команда, которую надо проверить.
    ignore - список. Список слов, которые надо игнорировать.
    Возвращает True, если в команде содержится слово из списка ignore, False - если не содержит.
    """
    for word in ignore:
        if word in command:
            return True
    return False


def config_to_dict(config):
    """
    config - имя конфигурационного файла коммутатора.
    Возвращает словарь:
    - Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
    - Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, в виде списка.
    - Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком.
    """
    ignore = ['duplex', 'alias', 'Current configuration']
    config_dict = {}
    current_command = None
    current_subcommands = []

    with open(config, 'r') as file:
        for line in file:
            line = line.strip()

            if line.startswith('!') or ignore_command(line, ignore):
                continue

            if not line.startswith(' '):
                if current_command:

                    if current_subcommands:
                        config_dict[current_command] = current_subcommands
                    else:
                        config_dict[current_command] = []

                current_command = line
                current_subcommands = []
            else:

                current_subcommands.append(line)


        if current_command:
            if current_subcommands:
                config_dict[current_command] = current_subcommands
            else:
                config_dict[current_command] = []

    return config_dict

config_dict = config_to_dict('config_sw1.txt')


for command, subcommands in config_dict.items():
    print(f'{command}:')
    for subcommand in subcommands:
        print(f'  {subcommand}')
    if not subcommands:
        print('  (Нет подкоманд)')
