def phone_number(num):
    string = [(str(x)) for x in num]
    string = ''.join(string)
    return f'({string[:3]}) {string[3:6]}-{string[6:]}'

print(phone_number([1,2,3,4,5,6,7,8,9,0]))
