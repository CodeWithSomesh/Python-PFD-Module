import random
import collections
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [collections.defaultdict(list) for _ in range(capacity)]
    def insert_item(self, key, data):
        index = self.hash_function(key)
        self.table[index][key].append(data)
    def delete_item(self, key):
        index = self.hash_function(key)
        if key in self.table[index]:
            self.table[index].pop(key)
    def display_hash(self):
        for i in range(self.capacity):
            print(f"table[{i}]", end="")
            for key, values in self.table[i].items():
                for value in values:
                    print(f" --> {value}", end="")
            print()
    def hash_function(self, key):
        # print(key)
        #Initialize Variables
        sumOfKey = 0
        totalValue = 0
        finalHashValue = 0
        constantPrimeNumber = 47
        increment = 1

        # Seperating keys by numbers, then multiply the numbers by their ASCII Code and Index Value
        for i in str(key):
            index = str(key).index(i)
            sumOfKey += ord(i) * (int(i) * index)

        # print(sumOfKey)

        # Seperating sumOfKey by numbers,
        # then multiply the numbers by Index Value and by Prime Number,
        # then plus with the number's ASCII Code,
        # then plus everything with the Square of Increment
        for char in str(sumOfKey):
            index = str(sumOfKey).index(char)
            totalValue += (int(char) * index * constantPrimeNumber + ord(char)) + (increment * increment)
            constantPrimeNumber += 3
            increment += 2

        finalHashValue = totalValue % self.capacity
        # print(finalHashValue)
        return finalHashValue



# Example usage
key = [231, 321, 212, 321, 433, 262]
data = [123, 432, 523, 43, 423, 111]
size = len(key)

h = HashTable(size)
for i in range(size):
    h.insert_item(key[i], data[i])
h.delete_item(12)
h.display_hash()
