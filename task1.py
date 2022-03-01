# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import sys

script_name, prod, rate, bonus = sys.argv

print("Name of script: ", script_name)
print("Production: ", prod)
print("Rate: ", rate)
print("Bonus: ", bonus)
print("Employee salary: ", (int(prod) * int(rate)) + int(bonus))