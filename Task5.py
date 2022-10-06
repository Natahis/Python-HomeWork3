# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


num = int(input('Введите целое число: '))
def fib(num):
    if num in [1,2]:
        return 1
    else:
        if num > 0:
            return fib(num - 1) + fib(num - 2)
        else:
            return fib(num + 2) - fib(num + 1)     

list = []
for i in range(-num, num+1):
    list.append(fib(i))

fib(num)
print(list)
