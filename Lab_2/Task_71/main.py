import random


def print_board(board):
    print("-------------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-------------")


def check_winner(board, player):
    # Проверка столбцов и строк
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(cell == player for cell in [board[j][i] for j in range(3)]):
            return True
        
    # Проверка диагоналей
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False


def tic_tac_toe():
    # Инициализируем доску пустыми ячейками
    board = [[" "]*3 for _ in range(3)]
    players = ["X", "O"]
    current_player = random.choice(players)

    print("Начинающий игрок: ", current_player)
    while True:
        try:
            # Получение строки и столбца от игрока
            row = int(input("Введите номер строки (0-2) --> "))
            col = int(input("Введите номер столбца (0-2) --> "))

            if board[row][col] != " ":
                print("Клетка уже занята!")
                continue

            board[row][col] = current_player

            print_board(board)

            # Кто победил?
            if check_winner(board, current_player):
                print("Игрок ", current_player, " победил!")
                break

            # Меняем игрока
            if current_player == "X":
                current_player = players[1]
            else:
                current_player = players[0]

        except (ValueError, IndexError):
            print("Неверный ввод. Пожалуйста, введите число от 0 до 2.")


tic_tac_toe()
