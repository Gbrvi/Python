# Preenchimento 

# Precisará sempre da flag de alinhamento (< ^ >) e tam minimo

string = 'batata'

print(f'{string:-^25}')
# OUTPUT : ---------batata----------
print(f'{string:-<25}')
# OUTPUT : batata-------------------
print(f'{string:->25}')
# OUTPUT : -------------------batata


print(f'{string.upper()=!a:=^20}')
# OUTPUT : string.upper()======='BATATA'======

