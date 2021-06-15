# Smirnov Artem lesson 1 Dz 4


import random

print('Ведите границы для случайного целого числа:')
Num1 = int(input('Number 1 = '))
Num2 = int(input('Number 2 = '))

print('Ведите границы для случайного вещественного числа:')
Mat1 = float(input('Material 1 = '))
Mat2 = float(input('Material 2 = '))

print('Ведите границы для случайной буквы:')
Ch1 = input('char1 = ').upper()
Ch2 = input('char2 = ').upper()

r_int = random.randint(Num1, Num2)
r_float = random.uniform(Mat1, Mat2)
r_char = chr(random.randint(ord(Ch1), ord(Ch2)))

print(f'Случайное целое число: {r_int}\n'
      f'Случайное вещественное число: {r_float}\n'
      f'Случайная буква: "{r_char}"')