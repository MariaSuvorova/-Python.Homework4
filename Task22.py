"""Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются
 в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
m - кол-во элементов второго множества. Затем пользователь вводит сами 
элементы множеств. """

n = int(input("Введите количество 1 мн-ва:   "))
m = int(input("Введите количество 2 мн-ва:   "))
number_n = [int(i) for i in list(input("Введите 1 мн-во:  ").split())]
number_n = set(number_n)
number_m = [int(i) for i in list(input("Введите 2 мн-во:  ").split())]
number_m = set(number_m)
result = set.intersection(number_n, number_m)
result = list(result)
result.sort()
print(*result)


