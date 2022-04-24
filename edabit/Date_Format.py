def format_date(date):
    inverso = ''.join(date.split('/')[::-1])
    return inverso

print(format_date('11/12/2019'))
