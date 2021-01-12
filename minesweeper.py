from game import Game
from os import system
class Minesweeper:
    def __init__(self):
        diff, first_pos = self.initialize_game()
        if diff == 'e':
            self.ms = Game(9,9,10, first_pos)
        elif diff == 'm':
            self.ms = Game(16,16,40, first_pos)
        elif diff == 'h':
            self.ms = Game(16,30,99, first_pos)
        self.ms.uncover(first_pos[0], first_pos[1])
        print(self.ms)
        self.play()

    def display_fake_board(self, r,c):
        disp = [['_' for i in range(c+1)] for j in range(r+1)]
        disp[0][0] = ' '
        for i in range (1, c+1):
            disp[0][i] = i
        for i in range (1, r+1):
            disp[i][0] = i
        output = ''
        for row in disp:
            output = output + (' '.join([str(item).center(2) for item in row])) + '\n\n'
        print(output)


    def initialize_game(self):
        while True:
            print("Enter difficulty (easy, moderate, hard): e,m,h")
            diff = input()
            system('clear')
            if diff == 'e':
                self.display_fake_board(9,9)
                break
            elif diff == 'm':
                self.display_fake_board(16,16)
                break
            elif diff == 'h':
                self.display_fake_board(16,30)
                break
        while True:
            loc = input('Enter the cell to reveal:')
            inputs = loc.split(' ')
            if len(inputs) == 2:
                starting_pos = (int(inputs[0]), int(inputs[1]))
                system('clear')
                break

        return (diff, starting_pos)

    def play(self):
        while True:
            loc = input('Enter the cell to reveal/flag:')
            inputs = loc.split(' ')
            if len(inputs) == 2:
                r,c = (int(inputs[0]), int(inputs[1]))
                result = self.ms.uncover(r,c)
                if result == 0:
                    print('YOU LOSE')
                    print(self.ms)
                    break
                elif result == 2:
                    print('YOU WIN')
                    break
            if len(inputs) == 3:
                r,c = (int(inputs[1]), int(inputs[2]))
                result = self.ms.flag(r, c)
                if result == 2:
                    print('YOU WIN')
                    break
            system('clear')
            print(self.ms)

def main():
    obj = Minesweeper()

if __name__ == '__main__':
    main()
