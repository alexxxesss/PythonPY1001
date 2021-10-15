speed = int(input("Введите вашу скорость передачи данных по локальной сети (б/с): "))
time = int(input('Введите время, которое потребовалось чтобы скачать игру (мин): '))
coast = int(input('Введите стоимость за Гбайт (руб): '))

size = speed * time * 60 / 1024 / 1024 / 1024
coast_size_for_game = (size - 1)

print("Размер файла: " + str(size))

if size > 1:
    coast_for_game = coast_size_for_game * coast
    print("Ученик заплатит " + str(coast_for_game) + " рублей")
else:
    print("Ученик ничего не заплатит")