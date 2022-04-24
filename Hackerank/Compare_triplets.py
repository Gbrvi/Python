# Sem zip
a = [17, 28, 30]
b = [99, 16, 8]

alice = 0
bob = 0

# for i in range(len(a)):
#     if a[i] > b[i]:
#         alice += 1
#     elif a[i] < b[i]:
#         bob += 1

# print(alice, bob)

#Com Zip

for x, y in zip(a, b):
    if x > y:
        alice += 1
    elif x < y:
        bob += 1

print(alice, bob)



