import random

def generate_random_ic():
    return ''.join(random.choices('0123456789', k=12))

def custom_hash_function(icNumber):
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
    tableSize = 3001
    hashCode = (totalSum * constantPrimeNumber) % tableSize

    return hashCode


def given_hash_function(ic_number):
    return int(ic_number) % 3001

def insert_into_hash_table(hash_table, ic_number, hash_function):
    index = hash_function(ic_number)
    if hash_table[index] is None:
        hash_table[index] = [ic_number]
    else:
        hash_table[index].append(ic_number)

def create_hash_table(size):
    return [None] * size


num_ic_numbers = 2000
hash_table_size = 3001

# Generate 2000 random 12-digit IC numbers
ic_numbers = [generate_random_ic() for _ in range(num_ic_numbers)]

# Create hash tables for both hash functions
custom_hash_table = create_hash_table(hash_table_size)
given_hash_table = create_hash_table(hash_table_size)

# Insert IC numbers into the custom hash table
for ic in ic_numbers:
    insert_into_hash_table(custom_hash_table, ic, custom_hash_function)

# Insert IC numbers into the given hash table
for ic in ic_numbers:
    insert_into_hash_table(given_hash_table, ic, given_hash_function)

# Output the hash tables (for demonstration purposes, this will only print non-empty chains)
# print("Custom Hash Table:")
# for i, chain in enumerate(custom_hash_table):
#     if chain:
#         print(f"Index[{i}]", end="")
#         for elements in chain:
#             print(f" --> {elements}", end="")
#         print()
#
#
# print("\nGiven Hash Table:")
# for i, chain in enumerate(given_hash_table):
#     if chain:
#         print(f"Index[{i}]", end="")
#         for elements in chain:
#             print(f" --> {elements}", end="")
#         print()
num = 1
print("Custom Hash Table:")
for i, chain in enumerate(custom_hash_table):

    if chain:
        if len(chain) > 1:
            print(f"{num}: {chain}")
            num += 1

num1 = 1
print("\nGiven Hash Table:")
for i, chain in enumerate(given_hash_table):

    if chain:
        if len(chain) > 1:
            print(f"{num1}: {chain}")
            num1 += 1



