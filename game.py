from board import Board

class Game:
    def __init__(self, r, c, num, first_pos):
        self.game = Board(r, c, num, first_pos)
        self.display = self.make_display_board(c,r)
        self.size = (r+1, c+1)
        self.flags_to_go = self.game.mines[:]
    def __str__(self):
        output = ''
        for row in self.display:
            output = output + (' '.join([str(item).center(2) for item in row])) + '\n\n'
        return output

    def make_display_board(self, c, r):
        disp = [['_' for i in range(c+1)] for j in range(r+1)]
        disp[0][0] = ' '
        for i in range (1, c+1):
            disp[0][i] = i
        for i in range (1, r+1):
            disp[i][0] = i
        return disp

    def flag(self, i, j):
        if i-1 >= self.game.size[0] or j-1 >= self.game.size[1]:
            return False
        else:
            if (i,j) in self.flags_to_go:
                self.flags_to_go.remove((i,j))
            if self.display[i][j] == '*':
                self.display[i][j] = '_'
            elif self.display[i][j] == '_':
                self.display[i][j] = '*'
            if self.game_won():
                return 2
            else:
                return 1

    def uncover(self, i, j):
        if i-1 >= self.game.size[0] or j-1 >= self.game.size[1]:
            return -1
        else:
            if self.game.board[i-1][j-1] == 'M':
                self.uncover_all(i,j)
                return 0

            elif self.game.board[i-1][j-1] == '_':
                self.uncover_blank_spaces(i-1,j-1)
                if self.game_won():
                    return 2
                else:
                    return 1

            else:
                self.display[i][j] = self.game.board[i-1][j-1]
                return 1

    def uncover_all(self, i, j):
        for row in range (1, self.game.size[0]+1):
            for col in range (1, self.game.size[1]+1):
                if self.game.board[row-1][col-1] == '_':
                    self.display[row][col] = ' '
                else:
                    self.display[row][col] = self.game.board[row-1][col-1]
        self.display[i][j] = 'X'


    def uncover_blank_spaces(self, r, c):
        q = set()
        q.add((r,c)) # board notation
        to_uncover = set() # game notation
        blank_cells = self.game.blanks # board notation

        while len(q) != 0:
            i,j = q.pop()
            to_uncover.add((i+1, j+1))
            for blank in blank_cells:
                if abs(blank[0]-i) <= 1 and abs(blank[1]-j) <= 1:
                    q.add((blank[0], blank[1]))
                    blank_cells.remove(blank)

        for cell in to_uncover:
            self.display[cell[0]][cell[1]] = ' '

        for cell in to_uncover:
            i,j = cell
            u_row = i-1 if i-1 >=1 else None
            l_col = j-1 if j-1 >=1 else None
            d_row = i+1 if i+1 < self.size[0] else None
            r_col = j+1 if j+1 < self.size[1] else None

            if u_row is not None and l_col is not None and self.display[u_row][l_col] == '_':
                self.display[u_row][l_col] = self.game.board[u_row-1][l_col-1]

            if u_row is not None and j is not None and self.display[u_row][j] == '_':
                self.display[u_row][j] = self.game.board[u_row-1][j-1]

            if u_row is not None and r_col is not None and self.display[u_row][r_col] == '_':
                self.display[u_row][r_col] = self.game.board[u_row-1][r_col-1]

            if i is not None and l_col is not None and self.display[i][l_col] == '_':
                self.display[i][l_col] = self.game.board[i-1][l_col-1]

            if i is not None and r_col is not None and self.display[i][r_col] == '_':
                self.display[i][r_col] = self.game.board[i-1][r_col-1]

            if d_row is not None and l_col is not None and self.display[d_row][l_col] == '_':
                self.display[d_row][l_col] = self.game.board[d_row-1][l_col-1]

            if d_row is not None and j is not None and self.display[d_row][j] == '_':
                self.display[d_row][j] = self.game.board[d_row-1][j-1]

            if d_row is not None and r_col is not None and self.display[d_row][r_col] == '_':
                self.display[d_row][r_col] = self.game.board[d_row-1][r_col-1]

    def game_won(self):
        return len(self.flags_to_go) == 0

def main():
    g = Game(16,30,99)
    print(g.game)
    print(g)
    a = input()
    b = input()
    g.uncover(int(a),int(b))
    print(g)

if __name__ == '__main__':
    main()
