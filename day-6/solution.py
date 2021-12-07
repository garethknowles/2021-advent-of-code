#!/usr/bin/env python3

import time

from functools import reduce

with open((__file__.rstrip("solution.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()
data = [str(line) for line in input.splitlines()]
test_data = [
    '3,4,3,1,2'
]

DEBUG = False

def incrementFish(f):
    return 6 if f  < 1 else (f - 1)

def runDay(fish):
    numberToAdd = sum(f == 0 for f in fish)
    fish = [incrementFish(f) for f in fish]
    new_fish = [8] * numberToAdd
    return fish + new_fish

def runDayConcurrent(fish):
    new_fish = [8] * sum(f == 0 for f in fish)
    fish = list(map(incrementFish, fish))
    return fish + new_fish

def calculate(input, days):
    fish = list(map(int, input[0].split(',')))
    for _ in range(0, days):
        fish = runDay(fish)
    return len(fish)

def calculateConcurrent(input, days):
    fish = list(map(int, input[0].split(',')))
    for _ in range(0, days):
        fish = runDayConcurrent(fish)
    return len(fish)

def part1(input):
    start = time.time()
    res = calculate(input, 80)
    elapsed = time.time() - start
    print("Completed in {} seconds".format(elapsed))

    start = time.time()
    res = calculateConcurrent(input, 80)
    elapsed = time.time() - start
    print("Completed in {} seconds".format(elapsed))

    return res

def part2(input):
    return calculate(input, 256)

print("Part 1 Test Output:")
print(str(part1(test_data)))
print("Part 1 Output:")
print(str(part1(data)))

# print("Part 2 Test Output:")
# print(str(part2(test_data)))
# print("Part 2 Output:")
# print(str(part2(data)))


