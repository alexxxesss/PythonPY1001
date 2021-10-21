# TODO

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

square_summ = (a + b)**2
summ_sqyare = a**2 + b**2

if square_summ > summ_sqyare:
    print("Квадрат суммы чисел " + str(a) + " и " + str(b) + " больше суммы квадратов этих же чисел")
else:
    print("Сумма квадратов чисел " + str(a) + " и " + str(b) + " больше квадрата суммы этих же чисел")
