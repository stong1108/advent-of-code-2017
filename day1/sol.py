class Solution(object):

    def __init__(self):
        self.total = 0
        self.digits = None

    def read_input(self, filename):
        with open(filename, 'rb') as f:
            self.digits = map(int, list(f.read().strip()))

    def go_through_digits(self):
        self.total = 0
        # add first digit to the end
        self.digits.append(self.digits[0])

        # pass through list
        last_digit = self.digits[0]
        for digit in self.digits[1:]:
            if digit == last_digit:
                self.total += digit
            last_digit = digit

    def skip_through_digits(self):
        self.total = 0
        # only use lists of even length
        l = len(self.digits)
        if l % 2 == 1:
            self.digits.pop()

        # pass through list halves simultaneously
        offset = l / 2
        for ind, digit in enumerate(self.digits[:offset]):
            if digit == self.digits[ind+offset]:
                self.total += 2*digit

if __name__ == '__main__':
    s = Solution()
    s.read_input('input.txt')
    s.go_through_digits()
    print 'Part 1 solution: {}'.format(s.total)
    s.skip_through_digits()
    print 'Part 2 solution: {}'.format(s.total)
