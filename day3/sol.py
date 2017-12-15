from math import floor, sqrt


class Solution(object):

    def __init__(self):
        self.x_dist = 0 # relative to `1`
        self.y_dist = 0 # relative to `1`

    def calc_steps(self, square_id):
        # find largest square size up until square_id
        square_dim = int(floor(sqrt(square_id)))
        leftover = square_id - square_dim**2

        # spiral around until you reach square_id
        if square_dim % 2 == 0: # start at top left corner
            self._start_from_top_left_corner(square_dim, leftover)
        else:
            self._start_from_bottom_right_corner(square_dim, leftover)

        # manhattan distance
        return abs(self.x_dist) + abs(self.y_dist)

    def _start_from_top_left_corner(self, square_dim, leftover):
        # corner coords
        self.x_dist = -(square_dim/2 - 1)
        self.y_dist = square_dim/2

        if leftover < (square_dim+1): # not enough leftover to make a full column side
            self.y_dist -= leftover - 1
            self.x_dist -= 1

        else: # enough to fill column side, go through row
            self.y_dist -= square_dim
            self.x_dist += leftover % (square_dim+1) - 1

    def _start_from_bottom_right_corner(self, square_dim, leftover):
        # corner coords
        self.x_dist = (square_dim-1)/2
        self.y_dist = -(square_dim-1)/2

        if leftover < (square_dim+1): # not enough leftover to make a full column side
            self.y_dist += leftover + 1
            self.x_dist += 1

        else: # enough to fill column side, go through row
            self.y_dist += square_dim
            self.x_dist -= leftover % (square_dim+1) + 1


if __name__ == '__main__':
    s = Solution()
    print 'Part 1 solution: {}'.format(s.calc_steps(312051))
