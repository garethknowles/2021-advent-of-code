#!/usr/bin/env python3
from functools import reduce
from statistics import multimode

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

def getDigit(position):
    def digit(input): return input[position]
    return digit

def filterByDigit(position, expected):
    def filter(input):
        return True if input[position] == expected else False
    return filter

def mostCommonVal(input, digit):
    most_common_list = multimode(map(getDigit(digit), input))
    return most_common_list[0] if len(most_common_list) == 1 else '1'

def oxyCalc(input, digit):
    if len(input) == 1: return input[0]    
    most_common = mostCommonVal(input, digit)
    new_list = list(filter(filterByDigit(digit, most_common), input))
    return oxyCalc(new_list, digit+1)

def co2Calc(input, digit):
    if len(input) == 1: return input[0]    
    least_common = '1' if mostCommonVal(input, digit) == '0' else '0'
    new_list = list(filter(filterByDigit(digit, least_common), input))
    return co2Calc(new_list, digit+1)

def part2(input):
    oxy = oxyCalc(input, 0)
    oxy_int = int(oxy, 2)
    co2 = co2Calc(input, 0)
    co2_int = int(co2, 2)
    return [oxy_int, co2_int, oxy_int*co2_int]


print("Part 1 Test Output:")
print(str(part1(test_data)))
print("Part 1 Output:")
print(str(part1(data)))

print("Part 2 Test Output:")
print(str(part2(test_data)))
print("Part 2 Output:")
print(str(part2(data)))
