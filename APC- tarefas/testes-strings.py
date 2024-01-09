# print('''Note que filter(function, iterable) é equivalente a expressão geradora (item for item in iterable if function(item)) se function não for None e (item for item in iterable if item) se function for None.''')
### 3 aspas para printar um texto longo ###

# teste= 'estou muito cansado...'
# div= teste.split()
# print(teste.strip())

#DESAFIOS:

#01:

# n1= input().strip()
# n2= n1.split()
# print(f'Nome maiusculo: {n1.upper()}')
# print(f'Nome minusculo: {n1.lower()}')
# print('Nº de letras:', len(n1.replace(' ','')))
# print(f'Nº letras do primeiro nome: {len(n2[0])}')

#02:

# n1= input()
# if len(n1)==1:
#     print('unidade:', n1)
# elif len(n1) == 2:
#     print('unidade:', n1[-1])
#     print('dezena:', n1[0])
# elif len(n1) == 3:
#     print('unidade:', n1[-1])
#     print('dezena:', n1[1])
#     print('centena:', n1[0])
# else:
#     print('unidade:', n1[-1])
#     print('dezena:', n1[2])
#     print('centena:', n1[1])
#     print('milhar:', n1[0])


#03:

# n1= input().split()
# if n1[0].upper() == 'SANTO':
#     print('O nome da cidade começa com "Santo"')
# else:
#     print('O nome da cidade não começa com "Santo"')

#04:

# n1= input()
# if 'silva' in n1.lower():
#     print(True)
# else:
#     print(False)

#05:

# n1= input()
# print('Nº de letras "A":', n1.lower().count('a'))
# print('Posição 1:', n1.lower().find('a') + 1)
# print('Ultima posição:', n1.lower().rfind('a')+1)

#06:

n= input().strip()
n1= n.split()
print('Primeiro:',n1[0].capitalize())
print('Ultimo:', n1[-1].capitalize())
