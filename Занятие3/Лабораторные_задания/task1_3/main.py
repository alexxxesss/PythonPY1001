if __name__ == "__main__":
    def prosto_func(n):

        list_prosto_multiplier = []
        for i in range(1, n):
            count = 0
            for x in range(1, i+1):
                if i % x == 0:
                    count += 1
            if count == 2:
                list_prosto_multiplier.append(i)

        list_multiplier = []

        while n != 1:
            for i in list_prosto_multiplier:
                while n % i == 0:
                    n /= i
                    list_multiplier.append(i)

        print(list_prosto_multiplier)

        return list_multiplier


    print(prosto_func(124))
