def normalize(string):
    if string.isupper():
        string = string.capitalize()
        string +=  '!'

    return string


print(normalize('CAPS LOCK DAY IS OVER'))
print(normalize('Today is not caps lock day'))

palavra = 'Today is not caps lock day'

print(palavra.isupper())



