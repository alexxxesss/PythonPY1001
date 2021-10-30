def func_mean(n, m):
    arithmetic_mean = sum(range(n, m)) / len(range(n, m))
    list_mean = [i for i in range(n, m) if i > arithmetic_mean]
    return list_mean


if __name__ == "__main__":

    n_1 = int(input("Введите число n: "))
    m_1 = int(input("Введите число m: "))

    print("-----")
    print(func_mean(n_1, m_1))
