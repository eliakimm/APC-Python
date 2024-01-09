#Questao 01:

# def imprimeTermos(n):
#     if n <= 0:
#         print(0)
#     else:
#         print(n)
#         imprimeTermos(n-2)

#Questao 02:

# def bomba(n,m,n2):
#     if n == 0:
#         print('Cabum!!!! Explodiu')
#     elif n == 5:
#         print('Seu tempo está acabando!')
#         bomba(n-1,m,n2)
#     elif n == 1 and m>=n2:
#         print('Bomba desativada automaticamente!')
#     elif n == 1 and n2>m:
#         print('Seja rápido. Falta 1 segundo')
#         bomba(n-1,m,n2)
#     else:
#         print(f'Atenção faltam {n} segundos...')
#         bomba(n-1,m,n2)
# 
# n= int(input())
# m= int(input())
# n2= n
# bomba(n,m,n2)


#Questao 03:

# def controle(n,i):
#     if i == n:
#         print(f'Parabens Julie! Voce tomou todos os {n} comprimidos!')
#     elif i == 0:
#         controle(n,i+1)
#     else:
#         print(f'Voce ja tomou {i} comprimidos, restam {n-i}.')
#         controle(n,i+1)


#Questao 04:

# def JaChegou(n,frase):
#     if n == 1:
#         print(frase)
#     else:
#         print(frase)
#         JaChegou(n-1,frase)

#Questao 05:


