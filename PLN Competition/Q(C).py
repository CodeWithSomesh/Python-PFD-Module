# Initialize Variables

n = 0 #numbers of items in trolley
t = 0 #times takes for the cashier to process the item
c = 0 #item price
timeTaken = 0 # Time taken to steal items
minCost = 0 #minimum price Paul has to pay
itemsInTrolley = []

n = int(input())
if not (1 <= n <= 2000):
    print("Input out of range")
    exit()

for _ in range(n):
    t, c = map(int, input().split())
    if not (0 <= t <= 2000 and 1 <= c <= 10 ** 9):
        print("Input out of range")
        exit()
    itemsInTrolley.append((t, c))


itemsInTrolley.sort(key=lambda x: (x[1], x[0]))


for t, c in itemsInTrolley:
    if t == 0:
        minCost += c
    elif timeTaken <= t:
        minCost += c
        del itemsInTrolley[-1]

print(minCost)


