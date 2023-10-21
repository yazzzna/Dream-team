from random import choice
from time import sleep
from colorama import Fore, Style

print("Добро пожаловать в нашу коллекцию мини-игр!")
sleep(1) #задержка на 1 секнду, чтобы не было сплошного текста сразу
print("У нас есть несколько увлекательных игр, которые помогут тебе развлечься и провести время с пользой")
sleep(1)
print("В зависимости от твоих предпочтений, у нас найдется что-то для тебя!")
sleep(1)
print("Выбирай любую игру из списка ниже и наслаждайся игровым процессом:")
sleep(1)
print("1. Виселица: Угадай загаданное слово на русском языке, угадывая по одной букве за раз, но будь осторожен - у тебя ограниченное количество попыток.")
sleep(1)
print("2. Wordle: Угадай слово на русском языке из 5 букв за 6 или менее попыток.")
sleep(1)
print("3. Морской бой: Сумей сбить 5 кораблей за 10 попыток")

sleep(1)
rezim_game = input("Введите номер игры, в которую хотите сыграть: ")

if rezim_game == "1":
    hangman = (
    """
     ------
     |    |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |    |
     | 
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   
     |   
     |     
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |   
     |   
    ----------
    """)

    count_wrong = len(hangman) - 1 #макс количество ошибок
    words = ("вес","май", "арбуз","слово", "математика","любовь", "кирпич","стул", "ананас","кофта", "майка","бар", "компьютер","мышь", "пенал","тетрадь", "ручка","телефон", "серёжки","пульт", "еда","мафия", "каталог","библиотека", "мужчина", "игра", "программирование")

    word = choice(words)  # выбираем слово
    count_alf = "_" * len(word)  # Количество букв
    wrong = 0  # Количество неверных ответов
    user_alf = []  # Буквы уже угаданы
    
    while wrong < count_wrong and count_alf != word:
        print(hangman[wrong])  # Вывод висельника по индексу
        print("\nИспользованные буквы:\n", user_alf)
        print("\nСлово, которое нужно найти:\n", count_alf)

        alf = input("\n\nВведите свое предположение с маленькой буквы: ")  
        while alf in user_alf:
            print("Вы уже вводили букву", alf)  # Если буква уже вводилась ранее, то выводим 
            alf = input("Введите свое предположение с маленькой буквы: ")  
        
        user_alf.append(alf)
        
        if alf in word:  # Если введённая буква есть в загаданном слове, то выводим соответствующее сообщение
            print("\nДа!", alf, "есть в слове!")
            new = ""
            for i in range(len(word)):  # В цикле добавляем найденную букву в нужное место
                if alf == word[i]:
                    new += alf
                else:
                    new += count_alf[i]
            count_alf = new
        else:
            print("\nИзвините, буквы \"" + alf + "\" нет в слове.")  # Если буквы нет, то выводим соответствующее сообщение
            wrong += 1

    if wrong == count_wrong: 
        print(hangman[wrong])
        print("\nТебя повесили!")
    else:  
        print("\nВы угадали слово!")
    print("\nЗагаданное слово было \"" + word + '\"')

if rezim_game == "2":
    print("Вы выбрали игру Wordle")
    sleep(1)
    print("Основная цель игры — угадать спрятанное слово за 6 попыток. ")
    sleep(1)
    print("В каждую строку нужно ввести любое слово длиною 5 букв, чтобы узнать, какие буквы есть в искомом слове.")
    sleep(1)
    print("В зависимости от того, какое слово вы ввели, буквы будут выделены тремя цветами.")
    sleep(2)
    print(Fore.MAGENTA + "Буквы вообще нет в целевом слове.")
    print(Fore.YELLOW + "Буква есть в слове, но не на том месте.")
    print(Fore.GREEN + "Буква в слове и в правильном месте.")
    print(Style.RESET_ALL)
    sleep(2)

    words2 = ("ПИТОН", "ПЧЕЛА", "ВЕСНА", "МЫШКА", "ТЕАТР", "БЕГУН", "БИЗОН", "БОБЕР", "ВЫЕЗД", "ГЕНИЙ", "ГЛУБЬ", "ЖЕЛОБ", "ЖЕРЛО", "ЗВЕНО", "ЛОПУХ", "МУЛЯЖ", "ОБРЫВ", "ОЛЕНЬ", "РУБИН", "ХИМИЯ")
    word2 = choice(words2) # выбор слова
    rus_alp = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


    for guess_num in range(1, 7):
        guess = input(f"Предположение\n {guess_num}: ").upper() # игрок вводит слово

        if len(guess) != 5: # если длина слова не равна 5
            print("Нужно слово, состоящее из 5 букв!")
            break

        if guess == word2: # если игрок угадал слово
            print("Вы угадали слово!")
            break

        def show_guesses(guess, word2): #функция меняющая цвет букв в слове-предположении
            s = ''
            for i in range(len(word2)):
                if guess[i] == word2[i]:
                    s = s + (Fore.GREEN + guess[i])
                elif guess[i] in word2:
                    s = s + (Fore.YELLOW + guess[i])
                else:
                    s = s + (Fore.MAGENTA + guess[i])
            return s

        print(show_guesses(guess, word2)) #выводит введеное предположение с цветными буквами
        print(Style.RESET_ALL) #возвращает стиль текста к обычному

    else:
        print("Вы проиграли :(")
        print(f"Загаданное слово было: {word2}")

if rezim_game == "3":
    from random import randint

    Hidden_Pattern = [[' '] * 8 for x in range(8)]  # шаблоны для 1) скрытого корабля, 2) для угаданного корабля
    Guess_Pattern = [[' '] * 8 for x in range(8)]

    let_to_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}


    # печать доски для игры
    def print_board(board):
        print(' A B C D E F G H')
        print(' ***************')
        row_num = 1
        for row in board:
            print("%d|%s|" % (row_num, "|".join(row)))
            row_num += 1


    # местоположение для корабля; номер строки от 1 до 8, столбца А-З
    def get_ship_location():
        row = input('Введите номер строки от 1 до 8! ').upper()
        while row not in '12345678':
            print("Недействительно значение. Введите номер строки от 1 до 8.")
            row = input('Пожалуйста, введите номер от 1 до 8! ')
        column = input('Введите номер столбца A-H! ').upper()
        while column not in 'ABCDEFGH':
            print("Пожалуйста, введите значение от A-H! ")
            column = input('Введите номер столбца от A-H! ')
        return int(row) - 1, let_to_num[column]


    # Рандомно создаю корабли
    def create_ships(board):
        for ship in range(5):
            ship_r, ship_cl = randint(0, 7), randint(0, 7)
            while board[ship_r][ship_cl] == 'X':
                ship_r, ship_cl = randint(0, 7), randint(0, 7)
            board[ship_r][ship_cl] = 'X'


    # подсчет сбитых кораблей
    def count_hit_ships(board):
        count = 0
        for row in board:
            for column in row:
                if column == 'X':
                    count += 1
        return count


    # запуск игры
    create_ships(Hidden_Pattern)  # создаем скрытые корабли
    turns = 10  # количество ходов
    while turns > 0:
        print('Добро пожаловать в Морской бой!')
        print_board(Guess_Pattern)
        row, column = get_ship_location()
        # рассматрвиаем различные случаи
        if Guess_Pattern[row][column] == '-':
            print(' Вы уже угадали это ')
        elif Hidden_Pattern[row][column] == 'X':
            print(' Поздравляем, вы подбили корабль! ')
            Guess_Pattern[row][column] = 'X'
            turns -= 1
        else:
            print('Вы проиграли :(')
            Guess_Pattern[row][column] = '-'
            turns -= 1
        if count_hit_ships(Guess_Pattern) == 5:
            print("Поздравляем, Вы потопили все корабли !!! ")
            break
        print(' У вас осталось ' + str(turns) + ' попыток')
        if turns == 0:
            print('игра завершена, спасибо! ')
            break
