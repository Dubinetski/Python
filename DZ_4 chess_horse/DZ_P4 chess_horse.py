# Определить за сколько ходов шахматный конь может обойти всю доску.
# Доска размером 8*8. Пользователь задает начальную позицию коня.


# оценка рейтинга клетки - колличества доступных полей для движения
def rate_position(chess, x, y):
    rate = 0
    for i in range(8):
        # если клетка находится в пределах поля и еще не посещалась
        if 0 <= x + d_x[i] < board_size and 0 <= y + d_y[i] < board_size and chess[x + d_x[i]][y + d_y[i]] == -1:
            rate += 1
    return rate


# Движение коня по доске. Движение осуществляется в клетку с наименьшим "рейтингом"
def horse_step(chess, x, y, step=0):
    chess[x][y] = step  # обозначаем клетку номером хода
    choice = -1
    rate_choice = 10  # произвольное недостижимое значение вариантов ходов конем (>8)
    for i in range(8):
        if 0 <= x + d_x[i] < board_size and 0 <= y + d_y[i] < board_size and chess[x + d_x[i]][y + d_y[i]] == -1:
            rate = rate_position(chess, x + d_x[i], y + d_y[i])
            if 0 <= rate <= rate_choice:
                rate_choice = rate
                choice = i
    if rate_choice != 10:
        horse_step(chess, x + d_x[choice], y + d_y[choice], step + 1)


# ======================================
board_size = 8  # размер шахматной доски
chess_board = [[-1 for i in range(board_size)] for i in range(board_size)]  # заполнение поля -1
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

horse_step(chess_board, x_start - 1, y_start - 1)

stepCount = 0
for row in chess_board:
    for elem in row:
        print(elem, end='\t')
        if elem > stepCount:
            stepCount = elem
    print(end='\n')

print('\nStep count = ' + str(stepCount))
