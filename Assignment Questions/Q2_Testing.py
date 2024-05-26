ic_number = '123456789123'
array1 = []
sumOfChar = 0
totalSum = 0

part1 = int(ic_number[0:3])
part2 = int(ic_number[3:6])
part3 = int(ic_number[6:9])
part4 = int(ic_number[9:12])

print(part1)
print(part2)
print(part3)
print(part4)


array1.append(part1)
array1.extend([part2, part3, part4])

print(array1)
print()

for elements in array1:
    for char in str(elements):
        index = str(elements).index(char)
        sumOfChar += ord(char) * (int(char) * index)


    totalSum += sumOfChar

print(totalSum)
capacity = 10
hashCode = (totalSum * 7) % capacity
print(hashCode)