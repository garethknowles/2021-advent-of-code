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

def getConsecutivePairs(input):
    solution = []
    for n in range(0, len(input)-1):
        new_val = [input[n], input[n+1]]
        solution.append(new_val)
    return solution

def getConsecutiveTrios(input):
    solution = []
    for n in range(0, len(input)-2):
        new_val = [input[n], input[n+1], input[n+2]]
        solution.append(new_val)
    return solution

def part1(input):
    pairs = getConsecutivePairs(input)

    increases = 0
    for [a, b] in pairs :
        if b > a:
            increases +=1

    return increases

def part2(input):
    groups = getConsecutiveTrios(input)

    totals = []
    for [a, b, c] in groups :
        totals.append(a+b+c)

    total_pairs = getConsecutivePairs(totals)
    increases = 0
    for [a, b] in total_pairs :
        if b > a:
            increases +=1
    
    return increases

print("Part 1 Test Output:")
print(part1(testData))

print("Part 1 File Output:")
print(part1(fileByLines))

print("\nPart 2 Test Output:")
print(part2(testData))

print("Part 2 File Output:")
print(part2(fileByLines))