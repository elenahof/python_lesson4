# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа,
# а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

from math import factorial
num = int(input("Введите число для вычисления факториала: "))
def fact_calc(x):
     for i in range(x):
         print(i, end='! = ')
         yield factorial(i)

for a in fact_calc(num):
    print(a)