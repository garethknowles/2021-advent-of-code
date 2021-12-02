#!/usr/bin/env python3

import functools

with open((__file__.rstrip("solution.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()
data = [str(line) for line in input.splitlines()]
test_data = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2",
]

def transformInput(line):
    [direction, amount] = line.split(' ')
    amountInt = int(amount)
    if direction == 'forward':
        return [amountInt, 0]
    
    depth = amountInt if direction == 'down' else -amountInt
    return [0, depth]

def part1(input):
    movements = list(map(transformInput, input))
    horizontal = sum(j for _, j in movements)
    depth = sum(i for i, _ in movements)
    return horizontal * depth

def calculate(existing, input):
    [direction, amount] = input.split(' ')
    amountInt = int(amount)
    [horizontal, depth, aim] = existing
    if direction == 'up':
        aim -= amountInt
    if direction == 'down':
        aim += amountInt
    if direction == 'forward':
        horizontal += amountInt
        depth += (aim * amountInt)
    
    return [horizontal, depth, aim]
    

def part2(input):
    [horizontal, depth, _] = functools.reduce(calculate, input, [0, 0, 0])
    return horizontal * depth

print("Part 1 Test Output:\n" + str(part1(test_data)))
print("Part 1 Output:\n" + str(part1(data)))

print("Part 2 Test Output:\n" + str(part2(test_data)))
print("Part 2 Output:\n" + str(part2(data)))

