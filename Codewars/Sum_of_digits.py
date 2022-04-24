def digital_root(n):
    a = len(str(n))
    x = 0
    while a > 1:
        x = 0
        for num in str(n):
            x += int(num)
        n = x # Resutaldo da soma
        a -= 1
        
    return x 



print(digital_root(493193))