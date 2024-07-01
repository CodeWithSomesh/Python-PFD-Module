import os

# Returns user input that has been completely validated
def getNumInput(prompt):
    while True:
        userInput = input(prompt)
        if userInput.isdigit():
            return int(userInput)
        else:
            print("Error: Invalid input. Please enter a valid integer.")

# Returns user input that has been completely validated
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

# My Hash Function with my Custom Folding Technique
def hashFunction(icNumber, tableSize):
    #Initialize Variables
    icArray = []
    sumOfChar = 0
    totalSum = 0
    constantPrimeNumber = 7
    hashCode = 0
    hashValue = 0

    # Firstly, seperating the IC Numbers into 4 parts by slicing
    part1 = int(icNumber[0:3])
    part2 = int(icNumber[3:6])
    part3 = int(icNumber[6:9])
    part4 = int(icNumber[9:12])
    icArray.append(part1)
    icArray.extend([part2, part3, part4])

    # Getting the index of all the numbers in the icArray
    # Multiplying the ASCII Code of each number with the multiplication between the number and their index
    for elements in icArray:
        for char in str(elements):
            index = str(elements).index(char)
            sumOfChar += ord(char) * (int(char) * index)

        totalSum += sumOfChar

    # Finally get the Hash Code after multiplying a prime number
    hashCode = (totalSum * constantPrimeNumber)

    # After the modulus operation, we obtain the hash value, which identifies the specific bucket
    # in the hash table where the data should be placed
    hashValue = hashCode % tableSize


    return hashValue




if __name__ == "__main__":
    hashCode = 0
    hashCodeArray = []

    numberPrompt = 'How many IC Numbers would you like to enter: '
    num = getNumInput(numberPrompt)

    icNumberPrompt = f'Enter IC number without dashes (12 digits): '
    icNums = getIcInput(icNumberPrompt, num)

    tableSizePrompt = 'Enter Table Size: '
    tableSize = getNumInput(tableSizePrompt)

    for icNum in icNums:
        hashCode = hashFunction(icNum, tableSize)
        hashCodeArray.append(hashCode)

    for code in hashCodeArray:
        print(f"Bucket {code} is filled")


    print()
    print()
    os.system('pause')
    os.system('cls')


    #123123123123
    #213213213213
    #231231231231
    #321321321321
    #132132132132
    #312312312312


