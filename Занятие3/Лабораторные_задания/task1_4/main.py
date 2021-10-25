if __name__ == "__main__":
    def infinity(epsilon=0.0001):
        sum_ = 0
        n = 1
        while 1 / (2**n) > epsilon:
                sum_ += 1 / (2**n)
                n += 1

        return sum_

    print(infinity())