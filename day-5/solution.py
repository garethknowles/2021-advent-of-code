#!/usr/bin/env python3
import collections

with open((__file__.rstrip("solution.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()
data = [str(line) for line in input.splitlines()]
test_data = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]

def transformLine(input):
    [start, end] = input.split(' -> ')
    [x1, y1] = start.split(',')
    [x2, y2] = end.split(',')
    return [[int(x1), int(y1)], [int(x2), int(y2)]]

def filterDiagonal(line):
    [[x1, y1], [x2, y2]] = line
    return (x1 == x2) | (y1 == y2)

def pointsCovered(line):
    [[x1, y1], [x2, y2]] = line
    if abs(x1 - x2) == abs(y1 - y2):
        xSteps = 1 if x1 < x2 else -1
        ySteps = 1 if y1 < y2 else -1
        coveredPoints = []
        for step in range(0, abs(x1 - x2)+1):
            x = x1 + (step * xSteps)
            y = y1 + (step * ySteps)
            coveredPoints.append((x, y))
    elif x1 == x2:
        yRange = range(y1, y2+1) if y2 > y1 else range(y2, y1+1)
        coveredPoints = zip([x1 for _ in range(0, len(yRange))], yRange)
    elif y1 == y2:
        xRange = range(x1, x2+1) if x2 > x1 else range(x2, x1+1)
        coveredPoints = zip(xRange, [y1 for _ in range(0, len(xRange))])
    else:
        print('ERROR')

    return list(coveredPoints)

def part1(input):
    transformed = map(transformLine, input)
    filtered = filter(filterDiagonal, transformed)
    covered_points = map(pointsCovered, filtered)
    flat_covered_points = [item for list in covered_points for item in list]
    counts = collections.Counter(flat_covered_points)

    intersections = 0
    for a, b in list(counts):
        count = counts[(a, b)]
        if count > 1:
            intersections += 1
    return intersections


def part2(input):
    transformed = map(transformLine, input)
    covered_points = map(pointsCovered, transformed)
    flat_covered_points = [item for list in covered_points for item in list]
    counts = collections.Counter(flat_covered_points)

    intersections = 0
    for a, b in list(counts):
        count = counts[(a, b)]
        if count > 1:
            intersections += 1

    # for y in range(0, 10):
    #     row = "|" + str(y) + '| '
    #     for x in range(0, 10):
    #         if (x, y) in flat_covered_points:
    #             count = counts[(x,y)]
    #             row += str(count)
    #         else:
    #             row += '.'
    #     print(row)
    return intersections

print("Part 1 Test Output:")
print(str(part1(test_data)))
print("Part 1 Output:")
print(str(part1(data)))

print("Part 2 Test Output:")
print(str(part2(test_data)))
print("Part 2 Output:")
print(str(part2(data)))


