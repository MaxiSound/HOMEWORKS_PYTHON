# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Тот, кто берет последнюю конфету - проиграл.

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


# player vs computer
import random
from random import randint, choice

print(
    '"Игра с конфетами"\n'
    'В игре участвуют два игрока\n'
    'Первый ход определяется жеребьевкой.\n'
    'Игроки ходят, совершая ход друг после друга\n'
    'Правила игры\n'
    'У нас есть некоторое количество конфет\n'
    'За один ход можно забрать не более определенного количества конфет, о котором мы договоримся\n'
    'Тот, кому достанется последняя конфета - проиграл\n'
)

messages = ['твой ход брать конфеты.', 'возьми конфеты.',
            'сколько конфет берем?', 'бери еще.', 'твой ход.']
max_number_move = 0


def introduce_players():
    player1 = input('Игрок, представьтесь:\n')
    player2 = 'Компьютер'
    print(f'Очень приятно, сегодня ты играешь с {player2}')
    return [player1, player2]


def sweets_game(players):
    global max_number_move
    total_sweets = int(input('Сколько всего у нас конфет:\n'))
    max_number_move = int(
        input('Сколько конфет можно забрать за один ход?\n'))
    first = int(input(
        f'{players[0]}. Хочешь ходить первым нажми 1. Если не хочешь нажми любую другую клавишу\n'))
    if first != 1:
        first = 0
    return [total_sweets, max_number_move, int(first)]


max_move = max_number_move


def game_player_vs_computer(sweets, players, messages):
    global max_number_move
    count = sweets[2]

    while sweets[0] > 0:
        if sweets[0] == (max_number_move and sweets[0] < max_number_move and sweets[0] > 1):
            move = sweets[0] - 1
            print(f'Компьютер забирает {move} конфет.')

        elif not count % 2:
            move = random.randint(1, sweets[1])
            print(f'Компьютер забирает {move} конфет.')
        else:
            print(f'{players[0]}, {choice(messages)}')
            move = int(input())
            if move > sweets[0] or move > sweets[1]:
                print(
                    f'Можно взять не более {sweets[1]} конфет, у нас всего {sweets[0]} конфет.')
                chance = 2
                while chance > 0:
                    if sweets[0] >= move <= sweets[1]:
                        break
                    print(
                        f'Что-то пошло не так, у тебя осталось {chance} попытки.')
                    move = int(input())
                    chance -= 1
                else:
                    return print(f'Попыток не осталось. Game over, loser!')
        sweets[0] = sweets[0] - move
        if sweets[0] > 0:
            print(f'Осталось {sweets[0]} конфет.')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return players[not count % 2]


players = introduce_players()
sweets = sweets_game(players)

winer = game_player_vs_computer(sweets, players, messages)
if not winer:
    print('У нас нет победителя.')
else:
    print(f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')

# Пока писал код появилось пара идей как сделать красиво =)
