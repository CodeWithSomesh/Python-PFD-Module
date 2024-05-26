def getNumInput(prompt):
    while True:
        userInput = input(prompt)
        if userInput.isdigit():
            return int(userInput)
        else:
            print("Error: Invalid input. Please enter a valid integer.")

def getIcInput(prompt, iteration):
    icNumsArray = []
    num = 1
    while num <= iteration:
        userInput = input(prompt)
        if len(userInput) != 12:
            print("Error: Input must be exactly 12 digits. Please try again.")
            continue
        elif not userInput.isdigit():
            print("Error: Invalid input. Please enter a valid integer.")
            continue

        icNumsArray.append(userInput)

        num += 1

    return icNumsArray

def hashFunction(icNumber, capacity):
    sumOfChar = 0
    array1 = []
    totalSum = 0
    hashCode = 0
    constantPrimeNumber = 7

    part1 = int(icNumber[0:3])
    part2 = int(icNumber[3:6])
    part3 = int(icNumber[6:9])
    part4 = int(icNumber[9:12])
    array1.append(part1)
    array1.extend([part2, part3, part4])

    for elements in array1:
        for char in str(elements):
            index = str(elements).index(char)
            sumOfChar += ord(char) * (int(char) * index)

        totalSum += sumOfChar

    print(totalSum)
    hashCode = (totalSum * constantPrimeNumber) % capacity


    return hashCode




if __name__ == "__main__":
    hashCode = 0
    hashCodeArray = []

    numberPrompt = 'How many IC Numbers would you like to enter: '
    num = getNumInput(numberPrompt)
    # print(num)
    icNumberPrompt = 'Enter your IC number without dashes (12 digits): '
    icNums = getIcInput(icNumberPrompt, num)
    # for i in icNum:
    #     print(i)
    capacityPrompt = 'Enter Table Size: '
    capacity = getNumInput(capacityPrompt)

    for icNum in icNums:
        hashCode = hashFunction(icNum, capacity)
        hashCodeArray.append(hashCode)

    for code in hashCodeArray:
        print(code)

    #123123123123
    #213213213213
    #231231231231
    #321321321321
    #132132132132
    #312312312312
