def main():
    integerArray = []
    integerOver100Array = []

    for i in range(10):
        value = int(input(f"Enter Integer {i+1}: "))
        integerArray.append(value)

    for i in integerArray:
        if i > 100:
            integerOver100Array.append(i)

    print(f'Numbers in the array: {integerArray}')
    print(f'Numbers in the array that are greater than 100: {integerOver100Array}')
    print(f'Summation of those numbers: {sum(integerOver100Array)}')


if __name__ == "__main__":
    main()