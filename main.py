

import random

while True:
    player = int(input("1-камень, 2-ножницы, 3-бумага"))
    if player == 1:
        print("Вы выбрали камень")
    if player == 2:
        print("Вы выбрали ножницы")
    if player == 3:
        print("Вы выбрали бумагу")
    comp = random.randint(1, 3)
    if comp == 1:
        print("Комп выбрал камень")
    if comp == 2:
        print("Комп выбрал ножницы")
    if comp == 3:
        print("Комп выбрал бумагу")
    if player == comp:
        win = 0
    if player == 1 and comp == 2:
        win = 1
    if player == 1 and comp == 3:
        win = 2
    if player == 2 and comp == 1:
        win = 2
    if player == 2 and comp == 3:
        win = 1
    if player == 3 and comp == 1:
        win = 1
    if player == 3 and comp == 2:
        win = 2
    if win == 0:
        print("ничья")
    if win == 1:
        print("Победил игрок")
    if win == 2:
        print("Победил компьютер")




        # одно = присваивание, == равно строгое равно и он выбирает значение