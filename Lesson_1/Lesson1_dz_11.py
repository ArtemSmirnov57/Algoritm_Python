# Smirnov Artem lesson 1 Dz 1


num = int(input("Введите целое трехзначное число: "))
a = num // 100
b = (num % 100) // 10
с = num % 10
comp = a * b * с
sum = a + b + с
print(f'Для числа {num}, произведение цифр = {comp}, сумма цифр = {sum}.')