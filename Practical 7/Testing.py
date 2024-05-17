# import random
#
# alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# random_selection = random.sample(alphabets, 5)
# print(random_selection)
# new_string = '231'.join(random_selection)
#
# print(new_string)

# key = 123
# sumOfKey = 0
#
# for i in str(key):
#     print(i)
#     index = str(key).index(i)
#     print(index)
#     sumOfKey += ord(i) * (int(i) * index)










# def hash_function(self, key):
    #     hash_value = 0
    #     prime = 31
    #     increment = 0
    #     for k in str(key):  # Convert key to string for consistent hashing of integers and strings
    #         hash_value = (hash_value * prime + ord(k)) + (increment * increment)
    #         increment += 1
    #     return hash_value % self.capacity
