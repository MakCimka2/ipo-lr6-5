#Написать программу, которая:
#- Создаёт с помощью генератора списков, список случайных целых чисел от **-50** до **50** размером **25** элементов.
#- Находит количество положительных, отрицательных и нулевых элементов в списке.
#- Выводит значения и их (*положительных, отрицательных и нулевых*) количество вместе с процентом от общего количества.
#- Выводит самое большое и самое маленькое значение

import random
count_minus = 0
count_plus = 0 
count_zero = 0
protcent_count_minus = 0 
protcent_count_plus = 0
protcent_count_zero = 0
min = 0
max = 0 
spisok = [random.randint(-50, 50) for i in range(25)] # Создаем список с 25 рандомными числами от -50 до 50
for i in spisok: #Находим кол-во положительных, отрицательных, чисел равных нулю , а так же минимальное и максимальное значение
    if i < 0:
        count_minus +=1
        if i < min:
            min = i
    elif i > 0:
        if i > max: 
            max = i 
            count_plus +=1
    else:
        count_zero +=1
protcent_count_zero = (count_zero / 25 * 100 ) #Считаем проценты для равных 0
protcent_count_minus = (count_minus / 25 * 100 ) #Считаем проценты для отрицательных
protcent_count_plus = (count_plus / 25 * 100 ) #Считаем проценты для положительных

print(spisok) #Выводим все
print("Количество чисел, которые равны 0: ", count_zero)
print("Количество положительных чисел: ", count_plus)
print("Количество отрицательных чисел: ", count_minus)
print("Процен чисел равных 0: ", protcent_count_zero)
print("Процент положительных чисел: ", protcent_count_plus)
print("Процент отрицательных чисел: ", protcent_count_minus)
print("Минимальное значение: ", min)
print("Максимальное значение: ", max)
