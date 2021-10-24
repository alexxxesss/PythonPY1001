if __name__ == "__main__":
    def infinity(epsilon=0.0001):
        sum_ = 0
        n = 1
        while True:
            if 1 / (2**n) > epsilon:
                sum_ += 1 / (2**n)
                n += 1
            else:
                break
        return (sum_)
    print(infinity())