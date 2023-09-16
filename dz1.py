# Задача №10 На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
n = int(input("Input number of coins: "))
list_coins = []
for i in range (n):
    from random import randint
    list_coins.append(randint(0, 1))
print (list_coins)
tails = list_coins.count(0)
if len(list_coins) - tails < tails:
    print(f'You need to flip {len(list_coins) - tails} coin/s') 
else:
    print(f'You need to flip {tails} coin/s')