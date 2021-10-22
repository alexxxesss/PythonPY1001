# TODO
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

variant_1 = (a < 45) and (b >= 45) and (c >= 45)
variant_2 = (a >= 45) and (b < 45) and (c >= 45)
variant_3 = (a >= 45) and (b >= 45) and (c < 45)

if variant_1 or variant_2 or variant_3:
    print(f'Какое-то одно число меньше 45')
else:
    print(f"Или 2 числа меньше 45, или 3 числа меньше 45, или все числа больше 45")


