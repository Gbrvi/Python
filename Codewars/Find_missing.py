def find_misisng(sequence):
    pa = sequence[-1] - sequence[-2]
    for x in range(len(sequence) - 1):
        if sequence[x + 1] - sequence[x] != pa:
            return sequence[x] + pa

def find_missing_2(sequence):
    interval = (sequence[-1] - sequence[0])/len(sequence)   # Isso retornará o valor da razao
    for previous, item in enumerate(sequence[1:]):
        if item - sequence[previous] != interval:
            return item - interval
    

print(find_misisng([1, 2, 3, 4, 6, 7, 8, 9]))