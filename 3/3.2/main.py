import sys

filename = sys.argv[1]
with open(filename) as file:
    for line in file:
        if not line.startswith("!"):
            print(line, end="")
