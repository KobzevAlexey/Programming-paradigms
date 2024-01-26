class Game:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'  # Предполагаем, что 'X' будет первым игроком

    def display_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def get_move(self):
        while True:
            try:
                row = int(input('Введите номер строки (1-3): ')) - 1
                col = int(input('Введите номер столбца (1-3): ')) - 1
                if 0 <= row <= 2 and 0 <= col <= 2:
                    return row, col
                else:
                    print('Неверный ввод. Попробуйте еще раз.')
            except ValueError:
                print('Неверный ввод. Попробуйте еще раз.')

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print('Неверный ход. Попробуйте еще раз.')

    def check_win(self):
        # Проверяем строки на победу
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]

        # Проверяем столбцы на победу
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]

        # Проверяем диагонали на победу
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        # Если ничья
        if all(self.board[i][j] != ' ' for i in range(3) for j in range(3)):
            return 'Ничья'

        # Если игра продолжается
        return None

    def play_game(self):
        while True:
            self.display_board()
            row, col = self.get_move()
            self.make_move(row, col)
            result = self.check_win()
            if result:
                self.display_board()
                if result == 'Ничья':
                    print('Игра окончена. Ничья!')
                else:
                    print(f'Игра окончена. Победил игрок {result}!')
                break


game = Game()
game.play_game()
