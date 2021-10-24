def factorial(n):
    factor = 1
    for i in range(1, n+1):
        factor *= i
    return factor

if __name__ == "__main__":
    # Write your solution here
    print(factorial(10))