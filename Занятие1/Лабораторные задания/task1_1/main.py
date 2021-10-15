DAYS_OF_YEAR = 365  # количество дней в году

start_year = input('Введите свой год рождения: ')  # TODO запросить у пользователя год рождения
current_year = input('Введите текущий год: ')  # TODO запросить у пользователя текущий год

years = int(current_year) - int(start_year)
days = years * DAYS_OF_YEAR
print(days)
# TODO посчитать и распечатать количество прожитых дней
