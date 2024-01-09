#01:

# chamada= []
# for i in range(int(input())):
#     nome= input()
#     chamada.append(nome)
# chamada.sort(reverse= True)
# for pessoa in chamada:
#     print(pessoa)

#02:

# crewmates= []
# user= []
# for i in range(int(input())+1):
#     nomes= input()
#     user.append(nomes)
# sus= user[-1].split()
# for i in user[:-1]:
#     if i not in sus:
#         crewmates.append(i)
# print(*crewmates)

#03:

# lista_n= list(map(int, input().split()))
# n= int(input())
# 
# for i in lista_n:
#     if i%n == 0:
#         print(i, end=' ')

#04:

# n= list(map(int, input().split()))
# soma= n[0]
# for i in range(len(n)-1):
#     soma= soma * 2 + n[i+1] * 1/2
# print(f'{soma:.2f}')

#05:

# def paron(lista):
#     vogais= ['a','e','i','o','u']
#     l_pares= []
#     for i in lista:
#         c=0
#         for j in i.lower():
#             if j in vogais:
#                 c+= 1
#         if c%2 == 0:
#             l_pares.append(i)
#     return l_pares

#06:

# n= list(map(int, input().split()))
# n1,n2= map(int, input().split())
# print(list(n[n1:n2]))

#07:

# for i in range(int(input())):
#     frase= list(input().split())
#     frase.insert(0, 'Raimundo Nonato')
#     print(*frase)

#08:

###DEBUG

#09:

n, m= map(int, input().split())
maior= []
linhas= [list(map(int,input().split())) for _ in range(n)]
indice_1= []
indice_0= []
m_dis= 0
for i in range(len(linhas)):
    c= 0
    temp= []
    indice_1.append([])
    indice_0.append([])
    for j in range(len(linhas[i])):
        if linhas[i][j] == 0:
            c+= 1
            indice_1[i].append(j)
        elif linhas[i][j] == 1:
            temp.append((c,i,j+1))
            c= 0
    maior.append(max(temp))
    temp.clear()

distancia, fileira, posicao= max(maior)
posicao= posicao - (distancia +2)
if linhas[fileira][posicao] == 0:
    print(distancia)
else:
    if distancia%2 == 0:
        distancia= distancia //2
        print(distancia)
    else:
        distancia= (distancia//2) +1
        print(distancia)

#10:

# def fibo(n, cont):
#     cont[n] += 1
#     
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibo(n-1, cont) + fibo(n-2, cont)
# 
# def contagem():
#     n = int(input())
#     cont = [0] * (n + 1)
#     result = fibo(n, cont)
#     
#     print(f'Termo: {result}')
#     
#     print('Quantidades:')
#     for i in range(n + 1):
#         print(f'fibonacci({i}) - {cont[i]}')
# 
# contagem()
