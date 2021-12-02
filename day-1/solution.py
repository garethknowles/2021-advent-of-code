#!/usr/bin/env python3

with open((__file__.rstrip("solution.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

fileByLines = [int(line) for line in input.splitlines()]

testData = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]

def getConsecutiveGroups(input, groupSize):
    solution = []
    for x in range(0, len(input)-(groupSize-1)):
        new_val = []
        for y in range(0, groupSize):
            new_val.append(input[x+y])
        solution.append(new_val)
    return solution

def isBigger(a, b):
    return 1 if b > a else 0

def part1(input):
    pairs = getConsecutiveGroups(input, 2)
    return sum(isBigger(a, b) for [a, b] in pairs)

def part2(input):
    totals = list(map(sum, getConsecutiveGroups(input, 3)))
    total_pairs = getConsecutiveGroups(totals, 2)
    return sum(isBigger(a, b) for [a, b] in total_pairs)

print("Part 1 Test Output:")
print(part1(testData))

print("Part 1 File Output:")
print(part1(fileByLines))

print("\nPart 2 Test Output:")
print(part2(testData))

print("Part 2 File Output:")
print(part2(fileByLines))