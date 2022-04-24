from functools import reduce
def survivor(string, arr):
    string = list(string)
    for c in arr:
        string.pop(c)

    return ''.join(string)

print(survivor('zbkk', [0, 1]))

def last_survivor(letters, coords):
    for i in coords:
        strin = letters[:]

print(last_survivor('zbkgk', [0, 1]))

b = 'zbk'
c = [0, 1]

a = reduce(lambda w, c: w[:c] + w[c + 1], b, c)
print(a)