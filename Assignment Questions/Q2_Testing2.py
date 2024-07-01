import random
import datetime
import os
import math
import statistics

# Generate Random IC Numbers
def generateRandomIC_Numbers():
    today = datetime.date.today()  # Get the current date

    while True:
        # Generate random year, month, and day
        year = random.randint(0, today.year % 100)  # 00 to current year % 100
        month = random.randint(1, 12)  # 01 to 12
        day = random.randint(1, 31)  # 01 to 31

        # Create a date string in YYMMDD format
        date_str = f"{year:02d}{month:02d}{day:02d}"

        try:
            # Check if the generated date is valid and not in the future
            generated_date = datetime.datetime.strptime(date_str, "%y%m%d").date()
            if generated_date <= today:
                break
        except ValueError:
            # Invalid date, generate again
            continue

    # Generate the last 6 digits randomly
    last_6_digits = ''.join(random.choices('0123456789', k=6))

    return date_str + last_6_digits


# My Hash Function
def myHashFunction(icNumber, tableSize):
    # Initialize Variables
    icArray = []
    sumOfChar = 0
    totalSum = 0
    constantPrimeNumber = 7
    hashCode = 0
    hashValue = 0

    # Firstly, separating the IC Numbers into 4 parts by slicing
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


# Display Hash Table Brackets that are Occupied only
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


# Display Hash Table Performance Results
def calculatePerformanceMetrics(hashTable):
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

    return {
        "totalBuckets": totalBucketsNum,
        "emptyBuckets": emptyBucketNum,
        "occupiedBuckets": occupiedBucketNum,
        "bucketsWith1Key": bucket_with_1_key,
        "bucketsWith2Keys": bucket_with_2_keys,
        "bucketsWith3Keys": bucket_with_3_keys,
        "bucketsWith4Keys": bucket_with_4_keys,
        "bucketsWith5Keys": bucket_with_5_keys,
        "bucketsWith6Keys": bucket_with_6_keys,
        "bucketsWith7Keys": bucket_with_7_keys,
        "bucketsWith8Keys": bucket_with_8_keys,
        "bucketsWith9Keys": bucket_with_9_keys,
        "bucketsWith10Keys": bucket_with_10_keys,
        "numOfCollisions": numOfCollisions,
        "bucketsWithCollision": bucketsWithCollision,
        "collisionRate": collisionRate
    }


def displayPerformanceResults(performanceMetrics):
    print()
    print(f"Total Buckets: {performanceMetrics['totalBuckets']}")
    print(f"Empty Buckets: {performanceMetrics['emptyBuckets']}")
    print(f"Occupied Buckets: {performanceMetrics['occupiedBuckets']}")
    print(f"Buckets with 1 key: {performanceMetrics['bucketsWith1Key']}")
    print(f"Buckets with 2 keys: {performanceMetrics['bucketsWith2Keys']}")
    print(f"Buckets with 3 keys: {performanceMetrics['bucketsWith3Keys']}")
    print(f"Buckets with 4 keys: {performanceMetrics['bucketsWith4Keys']}")
    print(f"Buckets with 5 keys: {performanceMetrics['bucketsWith5Keys']}")
    print(f"Buckets with 6 keys: {performanceMetrics['bucketsWith6Keys']}")
    print(f"Buckets with 7 keys: {performanceMetrics['bucketsWith7Keys']}")
    print(f"Buckets with 8 keys: {performanceMetrics['bucketsWith8Keys']}")
    print(f"Buckets with 9 keys: {performanceMetrics['bucketsWith9Keys']}")
    print(f"Buckets with 10 keys: {performanceMetrics['bucketsWith10Keys']}")
    print(f"Total Number of Collisions: {performanceMetrics['numOfCollisions']}")
    print(f"Number of Buckets with Collisions: {performanceMetrics['bucketsWithCollision']}")
    print(f"Collision Rate: {performanceMetrics['collisionRate']:.2f}%")
    print()
    print()


# Display Hash Table Brackets that has Collisions
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
    numRuns = 10

    myHashResults = []
    givenHashResults = []

    for run in range(numRuns):
        print(f"Run {run + 1}/{numRuns}")

        # Generate Random IC Numbers
        icNumbersArray = [generateRandomIC_Numbers() for _ in range(totalIC_Numbers)]

        # Create Hash Tables
        myHashTable = createHashTable(hashTableSize)
        givenHashTable = createHashTable(hashTableSize)

        # Insert IC Numbers into My Hash Table
        for icNum in icNumbersArray:
            insertInHashTable(myHashTable, hashTableSize, icNum, myHashFunction)

        # Insert IC Numbers into Given Hash Table
        for icNum in icNumbersArray:
            insertInHashTable(givenHashTable, hashTableSize, icNum, givenHashFunction)

        # Collect performance metrics
        myHashResults.append(calculatePerformanceMetrics(myHashTable))
        givenHashResults.append(calculatePerformanceMetrics(givenHashTable))

    # Calculate average metrics
    avgMyHashResults = {key: statistics.mean([result[key] for result in myHashResults]) for key in myHashResults[0]}
    avgGivenHashResults = {key: statistics.mean([result[key] for result in givenHashResults]) for key in givenHashResults[0]}

    # Display average results
    print("<------------------------ My Hash Function Average Performance ------------------------>")
    displayPerformanceResults(avgMyHashResults)

    print("<------------------------ Given Hash Function Average Performance ------------------------>")
    displayPerformanceResults(avgGivenHashResults)


if __name__ == "__main__":
    main()
