# Smirnov Artem lesson 1 Dz 9


print('Ведите 3 разных числа:')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

computation = a + b + c - max(a, b, c) - min(a, b, c)

print(f'Число {computation} - среднее')