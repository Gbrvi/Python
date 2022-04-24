def solution(s):
    for x in s:
        if x.isupper():
            indice = s.index(x)
    b = ''.join(s[:indice])        
    a = ''.join(s[indice:])
    return f'{b} {a}'


print(solution('helloWorld'))

