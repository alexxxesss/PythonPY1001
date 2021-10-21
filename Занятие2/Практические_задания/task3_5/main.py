wind = int(input("Введите скорость ветра (м/с): "))

if 1 <= wind <= 4:
    print("Ветер слабый")
elif 5 <= wind <= 10:
    print("Ветер умеренный")
elif 11 <= wind <= 18:
    print("Ветер сильный")
elif wind >= 19:
    print("Ветер ураганный")

# TODO напишите с помощью if-elif-else условие проверки скорости ветра
