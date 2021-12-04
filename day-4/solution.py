#!/usr/bin/env python3

with open((__file__.rstrip("solution.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()
data = [str(line) for line in input.splitlines()]
test_data = [
    "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
    "",
    "22 13 17 11  0",
    "8  2 23  4 24",
    "21  9 14 16  7",
    "6 10  3 18  5",
    "1 12 20 15 19",
    "",
    "3 15  0  2 22",
    "9 18 13 17  5",
    "19  8  7 25 23",
    "20 11 10 24  4",
    "14 21 16 12  6",
    "",
    "14 21 17 24  4",
    "10 16 15  9 19",
    "18  8 23 26 20",
    "22 11 13  6  5",
    "2  0 12  3  7",
]


class Bingo:
    def __init__(self, rows):
        self.rows = [row.split() for row in rows]
        self.selected = []
        self.cols = [[] for _ in range(0, len(rows))]
        for x, col in enumerate(self.cols):
            for row in self.rows:
                col.append(row[x])

    def checkRowForMatches(self, row):
        matches = sum([1 if val in self.selected else 0 for val in row])
        return matches == len(row)

    def checkRowsAndCols(self):
        for row in self.rows:
            if self.checkRowForMatches(row):
                return True
        for col in self.cols:
            if self.checkRowForMatches(col):
                return True
        return False

    def checkNumber(self, number):
        self.selected.append(number)
        return self.checkRowsAndCols()

    def isNotSelected(self, val):
        return not val in self.selected

    def calculateScore(self):
        lastNumber = self.selected[-1]
        flattendRows = [val for sublist in self.rows for val in sublist]
        unmarkedVals = list(
            filter(self.isNotSelected, flattendRows))
        unmarkedValsInt = [int(x) for x in unmarkedVals]
        unmarkedTotal = sum(unmarkedValsInt)

        return int(lastNumber) * unmarkedTotal


def transformToBingoBoards(input):
    chunkedInput = [input[i:i+6] for i in range(0, len(input), 6)]
    boards = [Bingo(boardData[1:]) for boardData in chunkedInput]
    return boards


def part1(input):
    revealedNumbersInput = input[0].split(',')
    boardInput = input[1:]
    boards = transformToBingoBoards(boardInput)

    for i in revealedNumbersInput:
        for board in boards:
            if board.checkNumber(i):
                return board.calculateScore()

    return 'No-one won'


def part2(input):
    return 0


print("Part 1 Test Output:")
print(str(part1(test_data)))
print("Part 1 Output:")
print(str(part1(data)))

# print("Part 2 Test Output:")
# print(str(part2(test_data)))
# print("Part 2 Output:")
# print(str(part2(data)))
