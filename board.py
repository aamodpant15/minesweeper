from random import random

class Board:
    def __init__(self, r, c, num, first_pos):
        self.size = (r,c)
        self.num_mines = num
        self.board = [['_' for i in range(c)] for j in range(r)]
        self.blanks = []
        self.mines = []
        self.first_click = None
        self.init_board(first_pos[0]-1, first_pos[1]-1)

    def __str__(self):
        output = ''
        for row in self.board:
            output = output + (' '.join([str(item).center(2) for item in row])) + '\n\n'
        return output

    def add_mines(self,i,j):
        print(i,j)
        for some_num in range(self.num_mines):
            while True:
                a = int(random() * self.size[0])
                b = int(random() * self.size[1])
                if (a==i-1 and b==j-1) or (a==i-1 and b==j) or (a==i-1 and b==j+1) or (a==i+1 and b==j-1) or (a==i+1 and b==j) or (a==i+1 and b==j+1) or (a==i and b==j-1) or (a==i and b==j+1) or (a==i and b==j):
                    continue
                else:
                    if self.board[a][b] == '_':
                        self.board[a][b] = 'M'
                        self.mines.append((a+1, b+1))
                        break

    def add_nums(self):
        for r in range(self.size[0]):
            for c in range(self.size[1]):
                if self.board[r][c] != 'M':
                    num = 0
                    u_row = r-1 if r-1 >=0 else None
                    l_col = c-1 if c-1 >=0 else None
                    d_row = r+1 if r+1 < self.size[0] else None
                    r_col = c+1 if c+1 < self.size[1] else None

                    if u_row is not None and l_col is not None and self.board[u_row][l_col] == 'M':
                        num += 1
                    if u_row is not None and c is not None and self.board[u_row][c] == 'M':
                        num += 1
                    if u_row is not None and r_col is not None and self.board[u_row][r_col] == 'M':
                        num += 1
                    if r is not None and l_col is not None and self.board[r][l_col] == 'M':
                        num += 1
                    if r is not None and r_col is not None and self.board[r][r_col] == 'M':
                        num += 1
                    if d_row is not None and l_col is not None and self.board[d_row][l_col] == 'M':
                        num += 1
                    if d_row is not None and c is not None and self.board[d_row][c] == 'M':
                        num += 1
                    if d_row is not None and r_col is not None and self.board[d_row][r_col] == 'M':
                        num += 1

                    if num != 0:
                        self.board[r][c] = num

        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.board[i][j] == '_':
                    self.blanks.append((i,j))


    def init_board(self, i,j):
        self.add_mines(i,j)
        self.add_nums()

def main():
    game = Board(10,9, 5)
    game2 = Board(5,6,2)
    print(game)
    print(game2)

if __name__ == '__main__':
    main()
