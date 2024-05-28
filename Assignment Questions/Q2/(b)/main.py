import random
import os
import math

# Generate Random IC Numbers
def generateRandomIC_Numbers():
    return ''.join(random.choices('0123456789', k=12))


# My Hash Function
def myHashFunction(icNumber, tableSize):
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

    # print(totalSum)
    hashCode = (totalSum * constantPrimeNumber) % tableSize

    return hashCode


# Given Hash Function
def givenHashFunction(icNumber, tableSize):
    return int(icNumber) % tableSize


# Create Hash Table with the given size
def createHashTable(tableSize):
    return [None] * tableSize

# Insert IC Numbers that are Hashed, into specific Index of the Hash Table
def insertInHashTable(hashTable, hashTableSize, icNumber, hashFunction):
    indexNum = hashFunction(icNumber, hashTableSize)

    if hashTable[indexNum] is None:
        hashTable[indexNum] = [icNumber]
    else:
        hashTable[indexNum].append(icNumber)

def displayHashTable(hashTable):
    num = 1
    print()
    for index in range(len(hashTable)):
        data = hashTable[index]
        if data:
            print(f"{num}. Bucket[{index}]", end="")
            for elements in data:
                print(f" --> {elements}", end="")
            print()
            num += 1

    print()
    print()


def displayPerformanceResults(hashTable):
    totalBucketsNum = 0
    emptyBucketNum = 0
    occupiedBucketNum = 0
    bucket_with_1_key = 0
    bucket_with_2_keys = 0
    bucket_with_3_keys = 0
    bucket_with_4_keys = 0
    bucket_with_5_keys = 0
    bucket_with_6_keys = 0
    bucket_with_7_keys = 0
    bucket_with_8_keys = 0
    bucket_with_9_keys = 0
    bucket_with_10_keys = 0
    bucketsWithCollision = 0
    numOfCollisions = 0
    collisionRate = 0.00

    for index in range(len(hashTable)):
        totalBucketsNum += 1
        data = hashTable[index]
        if data:
            if len(data) == 1:
                bucket_with_1_key += 1
            elif len(data) == 2:
                bucket_with_2_keys += 1
            elif len(data) == 3:
                bucket_with_3_keys += 1
            elif len(data) == 4:
                bucket_with_4_keys += 1
            elif len(data) == 5:
                bucket_with_5_keys += 1
            elif len(data) == 6:
                bucket_with_6_keys += 1
            elif len(data) == 7:
                bucket_with_7_keys += 1
            elif len(data) == 8:
                bucket_with_8_keys += 1
            elif len(data) == 9:
                bucket_with_9_keys += 1
            elif len(data) == 10:
                bucket_with_10_keys += 1


            if len(data) > 1:
                numOfCollisions += (len(data) - 1)

        else:
            emptyBucketNum += 1


    occupiedBucketNum = totalBucketsNum - emptyBucketNum
    bucketsWithCollision = totalBucketsNum - emptyBucketNum - bucket_with_1_key
    collisionRate = (bucketsWithCollision / totalBucketsNum) * 100
    collisionRate = math.ceil(collisionRate * 100) / 100

    print()
    print(f"Total Buckets: {totalBucketsNum}")
    print(f"Empty Buckets: {emptyBucketNum}")
    print(f"Occupied Buckets: {occupiedBucketNum}")
    print(f"Buckets with 1 key: {bucket_with_1_key}")
    print(f"Buckets with 2 keys: {bucket_with_2_keys}")
    print(f"Buckets with 3 keys: {bucket_with_3_keys}")
    print(f"Buckets with 4 keys: {bucket_with_4_keys}")
    print(f"Buckets with 5 keys: {bucket_with_5_keys}")
    print(f"Buckets with 6 keys: {bucket_with_6_keys}")
    print(f"Buckets with 7 keys: {bucket_with_7_keys}")
    print(f"Buckets with 8 keys: {bucket_with_8_keys}")
    print(f"Buckets with 9 keys: {bucket_with_9_keys}")
    print(f"Buckets with 10 keys: {bucket_with_10_keys}")
    print(f"Total Number of Collisions: {numOfCollisions}")
    print(f"Number of Buckets with Collisions: {bucketsWithCollision}")
    print(f"Collision Rate: {collisionRate:.2f}%")
    print()
    print()


def displayCollisions(hashTable):
    num = 1
    print()
    for index in range(len(hashTable)):
        data = hashTable[index]
        if data:
            if len(data) > 1:
                print(f"{num}. Bucket[{index}]", end="")
                for elements in data:
                    print(f" --> {elements}", end="")
                print()
                num += 1
    print()
    print()

def main():
    # Initialize Variables
    totalIC_Numbers = 2000
    hashTableSize = 3001
    customHashTable = []
    givenHashTable = []
    icNumbersArray = []

    # Create 2 Hash Tables
    myHashTable = createHashTable(hashTableSize)
    givenHashTable = createHashTable(hashTableSize)


    # Generate Random IC Numbers and store it in an Array
    for i in range(totalIC_Numbers):
        icNum = generateRandomIC_Numbers()
        icNumbersArray.append(icNum)

    # For every IC Number in the array, turn it into a Hash Code, Find the Index of the HashCode in the Hash Table,
    # And finally Insert the IC Number to the specific index of the Hash Table
    # My Hash Table
    for icNum in icNumbersArray:
        insertInHashTable(myHashTable, hashTableSize, icNum, myHashFunction)

    # Given Hash Table
    for icNum in icNumbersArray:
        insertInHashTable(givenHashTable, hashTableSize, icNum, givenHashFunction)


    # Display My Hash Table Details
    print("<------------------------ My Hash Table Performance ------------------------>")
    displayPerformanceResults(myHashTable)

    print("<------------------------ My Hash Table Results ------------------------>")
    displayHashTable(myHashTable)

    print("<------------------------ My Hash Table Collisions ------------------------>")
    displayCollisions(myHashTable)

    print("<------------------------ My Hash Table Performance ------------------------>")
    displayPerformanceResults(myHashTable)

    os.system('pause')
    os.system('cls')



    # Display Given Hash Table Details
    print("<------------------------ Given Hash Table Performance ------------------------>")
    displayPerformanceResults(givenHashTable)

    print("<------------------------ Given Hash Table Results ------------------------>")
    displayHashTable(givenHashTable)

    print("<------------------------ Given Hash Table Collisions ------------------------>")
    displayCollisions(givenHashTable)

    print("<------------------------ Given Hash Table Performance ------------------------>")
    displayPerformanceResults(givenHashTable)



    os.system('pause')
    os.system('cls')


if __name__ == "__main__":
    main()







