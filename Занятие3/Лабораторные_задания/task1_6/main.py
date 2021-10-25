if __name__ == "__main__":
    def stipend(a, b, perc, months=10):

        sum_expens = 0

        for i in range(months):
            sum_expens += b
            b *= 1 + perc * 0.01

        money = sum_expens - a * months

        return money

    stipend_mouth = int(input('Введите ежемесячную стипендию студента: '))
    monthly_expenses = int(input('Введите расходы на проживание месяца: '))
    percent = int(input('Введите количество процентов, на которое увеличиваются ежемесячные расходы: '))
    number_months = int(input('Введите количество месяцев, которое нужно прожить студенту: '))

    print(f'Для того, чтобы прожить {number_months} месяцев,нужно иметь на кармне : {stipend(stipend_mouth, monthly_expenses, percent, number_months)} рублей')
