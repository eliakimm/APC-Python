#01:

# n= int(input())
# matriz_1= []
# matriz_2= []
# inicio= 0
# for i in range(n):
#     linha_1= []
#     for j in range(n):
#         if j == inicio or j == (n-1-inicio):
#             linha_1.append('X')
#         else:
#             linha_1.append('0')
#     matriz_1.append(linha_1)
#     inicio+= 1
# 
# for k in range(n):
#     linha_2= []
#     linha_2= input().split()
#     for l in range(n):
#         if linha_2[l] != 'X':
#             linha_2[l]= '0'
#     matriz_2.append(linha_2)
#     
# if matriz_2 == matriz_1:
#     print('O one piece eh real!')
# else:
#     print('Talvez o tesouro seja os amigos que fizemos no caminho')


#02:

# def ordem(lista, t):
#     n= len(lista)
#     for i in range(n):
#         for j in range(n):
#             if (lista[i][t]<lista[j][t]) or (lista[i][t] == lista[j][t] and (sum(lista[i])<sum(lista[j]))):
#                 temp= lista[i]
#                 lista[i]= lista[j]
#                 lista[j]= temp
#     return lista
# 
# n= int(input())
# t= int(input())
# lista= [list(map(int, input().split())) for _ in range(n)]
# 
# lista= ordem(lista, t)
# 
# for listas in lista:
#     print(*listas)

#03:

# n, m= map(int,input().split())
# q= int(input())
# area= []
# maior= 0
# cont= 0
# 
# for i in range(n):
#     linha= []
#     for j in range(m):
#         linha.append(0)
#     area.append(linha)
# 
# for k in range(q):
#     x,y= map(int,input().split())
#     for l in range(m):
#         if l != (y-1):
#             area[x-1][l]+= 1
#     for h in range(n):
#         area[h][y-1]+= 1
# 
# for x in range(n):
#     if max(area[x]) > maior:
#         maior= max(area[x])
# 
# for p in range(n):
#     for d in range(m):
#         if area[p][d] == maior:
#             cont+= 1
# 
# print(cont)

#04:

n, m, k= map(int, input().split())
q= map(int, input().split())
produtos= [list(map(int,input().split())) for _ in range(n)]
compras= []

for i in range(k):
    for j in range(n):
        if len(produtos[j]) == 0:
            break
        p= min(produtos[j])
        compras.append(p)
        produtos[j].remove(p)

if len(compras) < n*k:
    print('Nao')
else:
    if m - sum(compras) < 0:
        print('Nao')
    else:
        print('Sim')
