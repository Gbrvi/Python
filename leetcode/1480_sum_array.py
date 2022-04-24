def sum_array(num):
    c, lista = 0, []
    for a in num:
        c += a
        lista.append(c)


    return lista



print(list(sum_array([1, 2, 3, 4])))