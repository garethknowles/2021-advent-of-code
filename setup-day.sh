DAY=$1 

echo "Setting up for $DAY"

mkdir "day-$DAY"
cd "day-$DAY"

aocd $DAY 2021 > input.txt

echo "#!/usr/bin/env python3

with open((__file__.rstrip(\"solution.py\")+\"input.txt\"), 'r') as input_file:
    input = input_file.read()

output = [str(line) for line in input.splitlines()]

print(\"Part 1 Output:\" + str(output))
" >> solution.py

chmod +x solution.py

echo "Setup complete."
