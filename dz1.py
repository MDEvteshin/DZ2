# Задача №10 На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# n = int(input("Input number of coins: "))
# list_coins = []
# for i in range (n):
#     from random import randint
#     list_coins.append(randint(0, 1))
# print (list_coins)
# tails = list_coins.count(0)
# if len(list_coins) - tails < tails:
#     print(f'You need to flip {len(list_coins) - tails} coin/s') 
# else:
#     print(f'You need to flip {tails} coin/s')

# Задача №12. Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# s = int(input("Input sum of numbers: "))
# m = int(input("Input multiplication of numbers: "))
# a = 0
# if s > 2000 or m > 1000000:
#     print('The solution is impossible')
# else:
#     for x in range (s and m):
#         for y in range (s and m):
#             if x + y == s and x * y == m:
#                 a += 1
#                 print(f'Numbers which satisfying both conditions are {x, y}')
# if a == 0:
#     print('The solution is impossible')

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# n = int(input("Введите число для которого хотaите узнать целые степени двойки: "))
# x = 0
# while 2 ** x <= n:
#     print(f'2 в степени {x} = {2 ** x}')
#     x += 1