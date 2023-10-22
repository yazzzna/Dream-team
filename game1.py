from random import randint

Hidden_Pattern=[[' ']*8 for x in range(8)] #шаблоны для 1) скрытого корабля, 2) для угаданного корабля
Guess_Pattern=[[' ']*8 for x in range(8)]

let_to_num={'A':0,'B':1, 'C':2,'D':3, 'E':4, 'F':5, 'G':6, 'H':7}

#печать доски для игры
def print_board(board):
    print(' A B C D E F G H')
    print(' ***************')
    row_num=1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num +=1

#местоположение для корабля; номер строки от 1 до 8, столбца А-З
def get_ship_location():
    row=input('Введите номер строки от 1 до 8! ').upper()
    while row not in '12345678':
        print("Недействительно значение. Введите номер строки от 1 до 8.")
        row=input('Пожалуйста, введите номер от 1 до 8! ')
    column=input('Введите номер столбца A-H! ').upper()
    while column not in 'ABCDEFGH':
        print("Пожалуйста, введите значение от A-H! ")
        column=input('Введите номер столбца от A-H! ')
    return int(row)-1,let_to_num[column]

#Рандомно создаю корабли
def create_ships(board):
    for ship in range(5):
        ship_r, ship_cl=randint(0,7), randint(0,7)
        while board[ship_r][ship_cl] =='X':
            ship_r, ship_cl = randint(0, 7), randint(0, 7)
        board[ship_r][ship_cl] = 'X'

#подсчет сбитых кораблей
def count_hit_ships(board):
    count=0
    for row in board:
        for column in row:
            if column=='X':
                count+=1
    return count

#запуск игры
create_ships(Hidden_Pattern) #создаем скрытые корабли 
turns = 10 #количество ходов
while turns > 0:
    print('Добро пожаловать в Морской бой!')
    print_board(Guess_Pattern)
    row,column =get_ship_location()
    #рассматрвиаем различные случаи
    if Guess_Pattern[row][column] == '-':
        print(' Вы уже угадали это ')
    elif Hidden_Pattern[row][column] =='X':
        print(' Поздравляем, вы подбили корабль! ')
        Guess_Pattern[row][column] = 'X'
        turns -= 1
    else:
        print('Вы проиграли :(')
        Guess_Pattern[row][column] = '-'
        turns -= 1
    if  count_hit_ships(Guess_Pattern) == 5:
        print("Поздравляем, Вы потопили все корабли !!! ")
        break
    print(' У вас осталось ' +str(turns) + ' попыток')
    if turns == 0:
        print('игра завершена, спасибо! ')
        break