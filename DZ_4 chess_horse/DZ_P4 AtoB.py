# Программа находит минимальное колличество ходов конем до каждой из клеток шахматного поля
# из заданной пользователем клетки.


board_size = 8  # размер шахматной доски
chess_board = [[-1 for i in range(board_size)] for i in range(board_size)]  # заполнение клеток -1
print("Please enter the start coordinate of the chess horse.")
while True:
    try:
        x_start = int(input("X = "))
        y_start = int(input("Y = "))
        if 1 <= x_start <= 8 and 1 <= y_start <= 8:
            break
        else:
            print("Incorrect number. X and Y is from 1 to " + str(board_size))
    except ValueError:
        print("Warning! Enter the number from 1 to " + str(board_size))

d_x = [-2, -2, -1, -1, 1, 1, 2, 2]  # список смещений коня по Х
d_y = [1, -1, 2, -2, 2, -2, -1, 1]  # список смещений коня по Y


# заполнение клеток значениями минимального колличество шагов до них из исходной
def fill(chess, x, y, step=0):
    if chess[x][y] == -1 or chess[x][y] > step:
        chess[x][y] = step
    else:
        return

    for i in range(8):
        if 0 <= x + d_x[i] < board_size and 0 <= y + d_y[i] < board_size:
            fill(chess, x + d_x[i], y + d_y[i], step + 1)


fill(chess_board, x_start - 1, y_start - 1)

for i in range(board_size):
    print(chess_board[i])
