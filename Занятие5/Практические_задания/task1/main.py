if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print(matrix[row][col], end=" ")
        print()

    for row in range(len(matrix)):
        print(matrix[row], end=" ")
        print()
