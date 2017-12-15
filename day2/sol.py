from itertools import permutations

class Solution(object):

    def __init__(self):
        self.spreadsheet = None # list of int lists
        self.checksum_1 = 0
        self.checksum_2 = 0

    def read_input(self, filename):
        with open(filename, 'rb') as f:
            lines = f.readlines()
        self.spreadsheet = map(lambda x: map(int, x.split()), lines)

    def make_checksum_1(self):
        self.checksum_1 = sum([max(row) - min(row) for row in self.spreadsheet])
        return self.checksum_1

    def make_checksum_2(self):
        self.checksum_2 = sum([x/y if x%y==0 else 0 for row in self.spreadsheet for x,y in permutations(row, 2)])
        return self.checksum_2

if __name__ == '__main__':
    s = Solution()
    s.read_input('input.txt')
    print 'Part 1 solution: {}'.format(s.make_checksum_1())
    print 'Part 2 solution: {}'.format(s.make_checksum_2())
