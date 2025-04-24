##1

# N=int(input())
# matriz=[]
# cont=int(0)
# for i in range(N):
#     coluna=[]
#     for j in range(N):
#         if j == cont or j == (N-1-cont):
#             coluna.append('X')
#         else:
#             coluna.append('O')
#     matriz.append(coluna)
#     cont+=1
# matriz2=[]
# for k in range(N):
#     coluna2=[]
#     coluna2=input().split()
#     for l in range(N):
#         if coluna2[l] != 'X':
#             coluna2[l]='O'
#     matriz2.append(coluna2)
# if matriz2 == matriz:
#     print('O one piece eh real!')
# else:
#     print('Talvez o tesouro seja os amigos que fizemos no caminho')
    
##2

# def mysorted(lista,x):
#     i=0
#     while i<len(lista):
#         j=0
#         while j<len(lista):
#             if(lista[i][x]<lista[j][x]) or ((lista[i][x]==lista[j][x]) and sum(lista[i])<sum(lista[j])):
#                 temp=lista[i]
#                 lista[i]=lista[j]
#                 lista[j]=temp
#             j+=1
#         i+=1
#     return lista
# 
# n=int(input())
# t=int(input())
# lista=[]
# for i in range(n):
#     lista.append(input().split())
# for j in range(len(lista)):
#     for k in range(len(lista[j])):
#         lista[j][k]=int(lista[j][k])
# lista=mysorted(lista,t)
# for l in range(len(lista)):
#     for m in range(len(lista[l])):
#         lista[l][m]=str(lista[l][m])
# for o in range(len(lista)):
#     print(' '.join(lista[o]))

##3

N,M=input().split()
N=int(N)
M=int(M)
Q=int(input())
A=[]
for i in range(N):
    A.append([])
    for j in range(M):
        A[i].append(0)
for k in range(Q):
    x,y=input().split()
    x=int(x)
    y=int(y)
    for l in range(M):
        if l!=(y-1):
            A[x-1][l]+=1
    for m in range(N):
        A[m][y-1]+=1
maior=0
for n in range(N):
    for o in range(M):
        if A[n][o]>maior:
            maior=A[n][o]
cont=0
for p in range(N):
    for q in range(M):
        if A[p][q]==maior:
            cont+=1
print(cont)

##4

# N,M,K=input().split()
# N=int(N)
# M=int(M)
# K=int(K)
# qtd=[]
# qtd.append(input().split())
# produtos=[]
# teste=0
# for i in range(N):
#     produtos.append(input().split())
# for j in range(N):
#     for k in range(len(produtos[j])):
#         produtos[j][k]=int(produtos[j][k])
# for l in  range(K):
#     for m in range(N):
#         if produtos[m]==[]:
#             teste=1
#             break
#         mini=produtos[m][0]
#         inc=0
#         for n in range(len(produtos[m])):
#             if produtos[m][n]<mini:
#                 mini=produtos[m][n]
#                 inc=n
#         produtos[m].pop(inc)
#         M-=mini
# if M<0 or teste==1:
#     print("Nao")
# else:
#     print("Sim")
        
##5

# comando=''
# grade=[['08:00 - 08:55','','','','','',''],['08:55 - 09:50','','','','','',''],['10:00 - 10:55','','','','','',''],['10:55 - 11:50','','','','','',''],['12:00 - 12:55','','','','','',''],['12:55 - 13:50','','','','','',''],['14:00 - 14:55','','','','','',''],['14:55 - 15:50','','','','','',''],['16:00 - 16:55','','','','','',''],['16:55 - 17:50','','','','','',''],['18:00 - 18:55','','','','','',''],['19:00 - 19:50','','','','','',''],['19:50 - 20:40','','','','','',''],['20:50 - 21:40','','','','','',''],['21:40 - 22:30','','','','','','']]
# while comando!='Hasta la vista, beibe!':
#     comando=input()
#     if comando=='?':
#         print('+---------------+----------+----------+----------+----------+----------+----------+')
#         print('|               | Seg      | Ter      | Qua      | Qui      | Sex      | Sab      |')
#         print('+---------------+----------+----------+----------+----------+----------+----------+')
#         for i in range(15):
#             if (grade[i][1]!='') or (grade[i][2]!='') or (grade[i][3]!='') or (grade[i][4]!='') or (grade[i][5]!='') or (grade[i][6]!=''):
#                 print(f'|{grade[i][0]:^{15}}|{grade[i][1]:^{10}}|{grade[i][2]:^{10}}|{grade[i][3]:^{10}}|{grade[i][4]:^{10}}|{grade[i][5]:^{10}}|{grade[i][6]:^{10}}|')
#                 print('+---------------+----------+----------+----------+----------+----------+----------+')
#     elif comando=='Hasta la vista, beibe!':
#         break
#     else:
#         op=comando[0]
#         cod=comando[2:10]
#         dth=comando[11:]
#         if ' ' in dth:
#             DTH=dth.split(' ')
#         else:
#             DTH=[]
#             DTH.append(dth)
#         if op=='+':
#             for k in range(len(DTH)):
#                 if 'M' in DTH[k]:
#                     d,h=DTH[k].split('M')
#                     for l in range(len(d)):
#                         for m in h:
#                             if grade[int(m)-1][int(d[l])-1]!='':
#                                 if l<1:
#                                     print(f'!({op} {cod} {DTH[k]})')
#                                 break
#                             else:
#                                 grade[int(m)-1][int(d[l])-1]=cod
#                 elif 'T' in DTH[k]:
#                     d,h=DTH[k].split('T')
#                     for l in range(len(d)):
#                         for m in h:
#                             if grade[int(m)+4][int(d[l])-1]!='':
#                                 if l<1:
#                                     print(f'!({op} {cod} {DTH[k]})')
#                                 break
#                             else:
#                                 grade[int(m)+4][int(d[l])-1]=cod
#                 elif 'N' in DTH[k]:
#                     d,h=DTH[k].split('N')
#                     for l in range(len(d)):
#                         for m in h:
#                             if grade[int(m)+10][int(d[l])-1]!='':
#                                 if l<1:
#                                     print(f'!({op} {cod} {DTH[k]})')
#                                 break
#                             else:
#                                 grade[int(m)+10][int(d[l])-1]=cod
#         elif op=='-':
#             for k in range(len(DTH)):
#                 if 'M' in DTH[k]:
#                     d,h=DTH[k].split('M')
#                     for l in range(len(d)):
#                         for m in h:
#                             if (grade[int(m)-1][int(d[l])-1]=='') or (grade[int(m)-1][int(d[l])-1]!=cod):
#                                 if l<1:
#                                     print(f'!({op} {cod} {DTH[k]})')
#                                 break
#                             else:
#                                 grade[int(m)-1][int(d[l])-1]=''
#                 elif 'T' in DTH[k]:
#                     d,h=DTH[k].split('T')
#                     for l in range(len(d)):
#                         for m in h:
#                             if (grade[int(m)+4][int(d[l])-1]=='') or (grade[int(m)+4][int(d[l])-1]!=cod):
#                                 if l<1:
#                                     print(f'!({op} {cod} {DTH[k]})')
#                                 break
#                             else:
#                                 grade[int(m)+4][int(d[l])-1]=''
#                 elif 'N' in DTH[k]:
#                     d,h=DTH[k].split('N')
#                     for l in range(len(d)):
#                         for m in h:
#                             if (grade[int(m)+10][int(d[l])-1]=='') or (grade[int(m)+10][int(d[l])-1]!=cod):
#                                 if l<1:
#                                     print(f'!({op} {cod} {DTH[k]})')
#                                 break
#                             else:
#                                 grade[int(m)+10][int(d[l])-1]=''

##6

# N,M,f=map(int, input().split())
# A=[]
# for i in range(N):
#     A.append(input().split())
# B=[]
# lin=0
# for i in range(int(N/f)):
#     col=0
#     n=[]
#     for j in range(int(M/f)):
#         cont=int(A[lin][col])
#         for k in range(f):
#             for l in range(f):
#                 if int(A[k+lin][l+col])>cont:
#                     cont=int(A[k+lin][l+col])
#         col+=(f)
#         n.append(str(cont))
#     B.append(n)
#     lin+=(f)
# for m in range(len(B)):
#     print(' '.join(B[m]))

##7

# N,M,K=map(int, input().split())
# times=input().split()
# agd=input().split()
# jogadores=[]
# for i in range(M):
#     jogadores.append(input().split())
# emp=[]
# for l in range(M):
#     emp.append([])
# for j in range(M):
#     for k in jogadores[j]:
#         if not(times[int(k)-1] in emp[j]):
#             emp[j].append(times[int(k)-1])
# man=[]
# for m in range(M):
#     test=0
#     for n in range(K):
#         if not(str((n+1)) in emp[m]):
#             test=1
#     if test==0:
#         man.append(m+1)
# if man==[]:
#     print(-1)
# else:
#     for o in range(len(man)):
#         print(man[o],end=" ")














