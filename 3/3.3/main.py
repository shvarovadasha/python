import sys

filename = sys.argv[1]

ignore = ['duplex', 'alias', 'Current configuration']
with open(filename) as file:
    for line in file:
        line_lower = line.lower()
        if not line.startswith("!") and not ('duplex' in line_lower or 'alias' in line_lower or 'current configuration' in line_lower):
            print(line, end="")
