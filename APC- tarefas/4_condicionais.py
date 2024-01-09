#Questao 01:

# n= int(input())
# if n%2 == 0:
#     print('Fome de comida! Queremos arroz e feijão')
# else:
#     print('Só um lanchinho cai bem!')

#Questao 02:

# n= input('O programa funciona?\n')
# if n == 'SIM':
#     n= input('Você entende o que fez?\n')
#     if n == 'SIM':
#         print('Ótimo. Então não mexe!')
#     else:
#         n= input('Já foi na tutoria?\n')
#         if n == 'SIM':
#             print('Choremos!')
#         else:
#             print('Temos um time a disposição!')
# else:
#     n= input('Você sabe onde está o erro?\n')
#     if n == 'SIM':
#         n= input('Acha que pode solucionar sozinho?\n')
#         if n == 'SIM':
#             print('Então mão na massa!')
#         else:
#             n= input('Já pesquisou no Google?\n')
#             if n == 'SIM':
#                 n= input('Já foi na tutoria?\n')
#                 if n == 'SIM':
#                     print('Choremos!')
#                 else:
#                     print('Temos um time a disposição!')
#             else:
#                 print('Corre lá então!')
#     else:
#         n= input('Já foi na tutoria?\n')
#         if n == 'SIM':
#             print('Choremos!')
#         else:
#             print('Temos um time a disposição!')

#Questao 03:

# x1= int(input())
# y1= int(input())
# x2= int(input())
# y2= int(input())
# 
# dis= (x1-x2)**2+(((y1-y2)**2))
# dis= dis **0.5
# 
# if dis <= 100:
#     print('É o amor da minha vida!')
# elif dis <= 200:
#     print('Talvez dê certo')
# else:
#     print('Não vale a pena investir')

#Questao 04:

# n1, n2, n3= map(int,input().split())
# tipo= input()
# 
# if tipo == 'P':
#     p1,p2,p3= map(int, input().split())
#     print(f'Ponderada\n{((n1*p1)+(n2*p2)+(n3*p3))/(p1+p2+p3):.2f}')
# elif tipo == 'A':
#     print(f'Aritmetica\n{(n1+n2+n3)/3:.2f}')
# elif tipo == 'H':
#     print(f'Harmonica\n{3/((1/n1)+(1/n2)+(1/n3)):.2f}')
# else:
#     print('Operacao inexistente')


#Questao 05:

#debug#

indiceReclamacao = int(input())
percentReclamResolPrim = int(input())
percentCliCancel = int(input())
indiceIndisponibilidade = int(input())
canceladoPorProblema = int(input())

if (percentReclamResolPrim >= 60):
    indice = indiceReclamacao - 5
else:
    indice = indiceReclamacao + 15
print(f'{indice}')

if ( percentCliCancel >= 10):
    if (canceladoPorProblema==0):
        indice = indice - 30
    else:
        indice = indice + 80
else:
    if (canceladoPorProblema==0):
        indice = indice - 10
    else:
        indice = indice + 50
print(f'{indice}');

if (indiceIndisponibilidade >= 10):
    indice = indice + 70
else:
    indice = indice - 20
print(f'{indice}')


