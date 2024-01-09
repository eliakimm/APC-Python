#01:

# nome= input()
# c= 0
# while nome != 'Fim':
#     c+= 1
#     nome= input()
# print(c)

#02:

# nome= input().split(',')
# sal= float(nome[1])
# quant= 0
# while sal > 0 :
#     quant+= 1
#     nome= input().split(',')
#     if nome[0] == 'Fim':
#         break
#     sal+= float(nome[1])
# if quant <= 0:
#     print(f'{0:.2f}')
# else:
#     print(f'{sal/quant:.2f}')

#03:

# nome,sal= input().split(',')
# sal= float(sal)
# maior= 0
# while nome != 'Fim':
#     if nome == 'Fim':
#         break
#     else:
#         if sal > maior:
#             maior= sal
#     nome,sal= input().split(',')
#     sal= float(sal)
# if maior == 0:
#     print('Não tem')
# else:
#     print(f'{maior:.2f}')

#04:

# nome, sal= input().split(',')
# sal= float(sal)
# menor= 10000000
# menor_sal= None
# while nome != 'Fim':
#     if nome == 'Fim':
#         break
#     else:
#         if sal <= menor:
#             menor= sal
#             menor_sal= nome
#     nome, sal= input().split(',')
#     sal= float(sal)
# if menor_sal == None:
#     print('Não tem')
# else:
#     print(menor_sal)

#05:

# n= int(input())
# maior= 0
# menor= 1000000000
# menor_sal= None
# maior_sal= None
# m= 0
# for i in range(n):
#     nome, sal= input().split(',')
#     sal= float(sal)
#     m+= sal
#     if sal >= maior:
#         maior= sal
#         maior_sal= nome
#     if sal <= menor:
#         menor= sal
#         menor_sal= nome
# if n == 0:
#     print('Não tem média\nNão tem\nNão tem')
# else:
#     print(f'{m/n:.2f}\n{maior_sal} {maior:.2f}\n{menor_sal} {menor:.2f}')

#06:

# n, m= map(int, input().split())
# c= 0
# for i in range(n):
#     grana= int(input())
#     c+=grana
# print(f'media: {c//n}')
# if c/n >= m:
#     print('o rock reinara mais uma vez')
# else:
#     print('rockeiros trabalhando ja')
    
    
#07:

# n= int(input())
# for i in range(0, n+1):
#     if i%3 == 0 and i%7 == 0:
#         print(i, end= ' ')

#08:

# a, b, ca, cb=  input().split()
# a= int(a)
# b= int(b)
# ca= float(ca)
# cb= float(cb)
# anos= 0
# while a < b:
#     a+= ((a*ca)//100)
#     b+= ((b*cb)//100)
#     anos+= 1
# if cb > ca:
#     print('A nunca alcancara B.')
# else:
#     if anos > 1000:
#         print('Mais de um milenio.')
#     else:
#         print(f'Vai alcancar em {anos} ano(s).')

#9:

def fibonacci(n):
    n1= 0
    n2, n3= 1, 1
    for i in range(n):
        print(n1, end= ' ')
        n1= n2
        n2= n3
        n3= n1 + n2

#10:

# def ehPrimo(n):
#     cont= 0
#     for i in range(1, n+1):
#         if n%i == 0:
#             cont+=1
#     if cont == 2:
#         return 1
#     else:
#         return 0
# 
# def divisoresPrimos(n):
#     cont= 0
#     for i in range(0, n):
#         if ehPrimo(i) == 1:
#             if n%i == 0:
#                 cont+= 1
#     return cont

