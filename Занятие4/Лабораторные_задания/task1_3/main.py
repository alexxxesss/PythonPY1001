def func_parity(n, m):
    list_parity = [i for i in range(n, m) if i % 2 == 0]
    return len(list_parity)


if __name__ == "__main__":

    n_1 = int(input("Введите число n: "))
    m_1 = int(input("Введите число m: "))

    print("-----")
    print(func_parity(n_1, m_1))