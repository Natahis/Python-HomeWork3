# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# my_list = [1.1, 1.2, 3.1, 5, 10.01]
# max_list = 0
# min_list = 1
# for i in my_list:
#      if i - int(i) >= max_list: max_list = i - int(i)
#      if i - int(i) < min_list: min_list = i - int(i)
# print((my_list), end= " => ")
# print(round(max_list - min_list,2))


# my_list = [1.1, 1.2, 3.1, 5, 10.01]
# new_list = []
# for i in my_list:
#     if i % 1 != 0:
#         new_list.append(round(i % 1, 2))
# max_list = max(new_list)
# min_list = min(new_list)
# print((my_list), end= " => ")
# print(round(max_list - min_list,2))

lst = [1.1, 1.2, 3.1, 5, 10.01]

lst = [round(val % 1, 2) for val in lst]
print(lst)
rev_result = max(lst) - min(lst)
print(max(lst))
print(min(lst))
print( rev_result)