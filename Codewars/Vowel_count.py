def get_count(input_str):
    return len([x for x in input_str if x in 'aeiouAERIOU'])

def get_count_2(input_str):
    return len([x for x in input_str if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'])

def get_count_3(input_str):
    return sum(1 for x in input_str if x in 'aeiouAEIOU' )

def get_count_4(input_str):
    return sum(x in 'aeiou' for x in input_str)

print(get_count('tk r n m kowrsuuiueoispkvgiw '))
print(get_count_2('aeioueueueueaeiou'))
print(get_count_3('aeieuueaeiou'))
print(get_count_4('abracadabra'))
