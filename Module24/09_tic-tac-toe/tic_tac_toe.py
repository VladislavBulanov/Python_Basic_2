class Cell:
    def __init__(self, number):
        self.number = number
        self.value = ' '

    def set_value(self, value):
        if self.value == ' ':
            self.value = value
            return True
        else:
            return False


class Board:
    def __init__(self):
        self.cells = [Cell(index) for index in range(1, 10)]

    def draw(self):
        print('-------------')
        for index in range(0, 9, 3):
            print('| {} | {} | {} |'.format(
                self.cells[index].value,
                self.cells[index + 1].value,
                self.cells[index + 2].value
            ))
            print('-------------')

    def check_win(self):
        # Check rows:
        for row in range(0, 9, 3):
            if self.cells[row].value == self.cells[row + 1].value == \
            self.cells[row + 2].value and self.cells[row].value != ' ':
                return True

        # Check columns:
        for col in range(3):
            if self.cells[col].value == self.cells[col + 3].value == \
            self.cells[col + 6].value and self.cells[col].value != ' ':
                return True

        # Check diagonals:
        if self.cells[0].value == self.cells[4].value == \
        self.cells[8].value and self.cells[0].value != ' ':
            return True
        elif self.cells[2].value == self.cells[4].value == \
        self.cells[6].value and self.cells[2].value != ' ':
            return True

        return False

    def is_full(self):
        for cell in self.cells:
            if cell.value == ' ':
                return False
        return True


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        while True:
            cell_number = input('{}, введите номер клетки (1-9): '.format(
                self.name
            ))
            if not cell_number.isdigit() or int(cell_number) not in range(1, 10):
                print('Вы ввели неверный номер клетки. Попробуйте ещё раз.\n')
            else:
                cell_number = int(cell_number)
                if board.cells[cell_number - 1].set_value(self.symbol):
                    break
                else:
                    print('Эта клетка уже занята. Попробуйте ещё раз.\n')
