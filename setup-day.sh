DAY=$1 

echo "Setting up for $DAY"

mkdir "day-$DAY"
cd "day-$DAY"

aocd $DAY 2021 > input.txt

echo "#!/usr/bin/env python3

with open((__file__.rstrip(\"solution.py\")+\"input.txt\"), 'r') as input_file:
    input = input_file.read()
data = [str(line) for line in input.splitlines()]
test_data = [

]

def part1(input):
    return 0

def part2(input):
    return 0

print(\"Part 1 Test Output:\")
print(str(part1(test_data)))
print(\"Part 1 Output:\")
print(str(part1(data)))

print(\"Part 2 Test Output:\")
print(str(part2(test_data)))
print(\"Part 2 Output:\")
print(str(part2(data)))

" >> solution.py

chmod +x solution.py

echo "Setup complete."
