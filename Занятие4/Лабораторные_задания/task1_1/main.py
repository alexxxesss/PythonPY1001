def func_sqrt(n, m):
    list_sqrt = [i ** 2 for i in range(n, m)]
    return list_sqrt


if __name__ == "__main__":

    n_1 = int(input("Введите число n: "))
    m_1 = int(input("Введите число m: "))

    print("-----")
    print(func_sqrt(n_1, m_1))
