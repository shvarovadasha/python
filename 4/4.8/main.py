def check_ignore(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.
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
    config - имя конфигурационного файла.
    Возвращает словарь с учетом всех уровней вложенности.
    """
    ignore = ['duplex', 'alias', 'Current configuration']
    config_dict = {}
    current_command = None
    current_subcommands = []
    current_level = config_dict

    with open(config, 'r') as file:
        for line in file:
            line = line.strip()

            if line.startswith('!') or check_ignore(line, ignore):
                continue


            if not line.startswith(' '):
                if current_command:

                    if current_subcommands:
                        current_level[current_command] = current_subcommands
                    else:
                        current_level[current_command] = []
                current_command = line
                current_subcommands = []

                if line.startswith('interface ') or line.startswith('router '):

                    current_level[line] = {}
                    current_level = current_level[line]
                else:
                    current_level = config_dict
            else:
                if current_level != config_dict:
                    subcommands_list = current_level.setdefault(current_command, [])
                    subcommands_list.append(line)
                else:

                    current_subcommands.append(line)

        if current_command:
            if current_subcommands:
                current_level[current_command] = current_subcommands
            else:
                current_level[current_command] = []

    return config_dict

config_dict = config_to_dict('config_r1.txt')

from pprint import pprint
pprint(config_dict)
