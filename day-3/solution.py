#!/usr/bin/env python3
from functools import reduce
from math import floor

with open((__file__.rstrip("solution.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()
data = [str(line) for line in input.splitlines()]
test_data = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010',
]


def reduction(digit, checkVal):
    def calculation(existing, input):
        val = int(input[digit])
        return existing + 1 if val == checkVal else existing
    return calculation


def flipBit(bit):
    return '1' if bit == '0' else '0'


def getCommonBits(input):
    mostCommonBits = []
    for i in range(0, len(input[0])):
        count = reduce(reduction(i, 1), input, 0)
        result = '1' if count > len(input)/2 else '0'
        mostCommonBits.append(result)
    leastCommonBits = list(map(flipBit, mostCommonBits))
    mostCommonBitsStr = ''.join(str(x) for x in mostCommonBits)
    leastCommonBitsStr = ''.join(str(x) for x in leastCommonBits)
    return [mostCommonBitsStr, leastCommonBitsStr]


def part1(input):
    [mostCommonBits, leastCommonBits] = getCommonBits(input)
    gamma_rate = int(mostCommonBits, 2)
    epsilon_rate = int(leastCommonBits, 2)
    return gamma_rate * epsilon_rate


def matches(i, common):
    def calc(input):
        return True if input[i] == common else False
    return calc


def oxgen_rating(input):
    remaining = input
    for i in range(0, len(remaining[0])):
        count = reduce(reduction(i, 1), input, 0)
        most_common = '1' if count < len(input)/2 else '0'
        remaining = list(filter(matches(i, most_common), input))
        if len(remaining) == 1:
            return remaining[0]

    return remaining[0]


def co2_rating(input):
    remaining = input
    for i in range(0, len(remaining[0])):
        count = reduce(reduction(i, 0), input, 0)
        least_common = '0' if count >= len(input)/2 else '1'
        remaining = list(filter(matches(i, least_common), input))
        if len(remaining) == 1:
            return remaining[0]

    return remaining[0]


def part2(input):
    oxy = oxgen_rating(input)
    co2 = co2_rating(input)
    return [oxy, co2]


print("Part 1 Test Output:")
print(str(part1(test_data)))
print("Part 1 Output:")
print(str(part1(data)))


print("Part 2 Test Output:")
print(str(part2(test_data)))
print("Part 2 Output:")
print(str(part2(data)))
