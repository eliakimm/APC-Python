tabela_peixes= []
peixe_menor= 10000000000
count= 0
nome_menor= None

while True:
    entrada= input().split()
    peixe= entrada[0]
    valor= float(entrada[1])
    count+= 1
    if valor < 0:
        break
    tabela_peixes.append((peixe,valor))
    
    if valor < peixe_menor:
        peixe_menor= valor
        nome_menor= peixe

print('+--------------------+--------------------+')
print('|        peixe       |      preço   R$    |')
print('+--------------------+--------------------+')

for peixe, valor in tabela_peixes:
    print(f'| {peixe:<18} | {valor:>18.2f} |')
    print('+--------------------+--------------------+')

if count > 2:
    print('')
    print('+-----------------------------------------+')
    print('|         Cambada de menor preço          |')
    print('+--------------------+--------------------+')
    print(f'| {nome_menor:<18} | {peixe_menor:>18.1f} |')
    print('+--------------------+--------------------+')
elif count <= 1:
    print('|           Hoje não tem peixe            |')
    print('+--------------------+--------------------+')