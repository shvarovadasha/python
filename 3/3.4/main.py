import sys

input_filename = sys.argv[1]
output_filename = sys.argv[2]

ignore = ['duplex', 'alias', 'Current configuration']
with open(input_filename) as infile, open(output_filename, 'w') as outfile:
    for line in infile:
        line_lower = line.lower()
        if not line.startswith("!") and not ('duplex' in line_lower or 'alias' in line_lower or 'current configuration' in line_lower):
            outfile.write(line)
