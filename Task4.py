# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


num = int(input('Введите целое положительное число: '))
result = 0
mult = 1


while num > 0:
    result = result + num % 2 * mult
    num = num // 2
    mult = mult * 10

print(result)


