start = 123  # Начало последовательности
stop = 9999  # Конец последовательности
krat = 23  # Число, кратность которому нужно найти числа в последовательности

spi_ = list(range(start, stop, krat))

print(spi_)
print('Количество чисел (по некорректному условию задачи), кратных ' + str(krat) + ' равно ' + str(len(spi_)))



spisok = list(range(start, stop))
spisok_krat = []
for i in range(len(spisok)):
    if spisok[i] % krat == 0:
        spisok_krat.append(spisok[i])

print(spisok_krat)
print('Количество реальных чисел, кратных ' + str(krat) + ' равно ' + str(len(spisok_krat)))
