'''
#Questao 01:

num= int(input())
print(f'{(num*100) +num}')
'''
'''
#Questao 02:

sabor, pedacos= input().split()
pedacos= int(pedacos)
print(f'Foram {pedacos} pedaços de bolo de {sabor}, então fica {3.25*pedacos:.2f} reais')
'''
'''
#Questao 03:

x= int(input())
print(f'{(x*2)-5+(2**x)}')
'''
'''
#Questao 04:

str1, str2, str3= input().split()
print(f'{str1 + str2*3+ str3*2}')
'''
'''
#Questao 05:

base  = int(input())
altura = int(input())
area = (base * altura)/2
print(f'{area:.2f}')
'''
'''
#Questao 06:

S = input()
O = input()
P = input()
print(f'{S} {P} {O}.')
'''
'''
#Questao 07:

n1, n2, n3= map(float, input().split())
p1, p2, p3= map(int, input().split())
print(f'{((n1*p1)+(n2*p2)+(n3*p3))/(p1+p2+p3):.6f}')
'''
'''
#Questao 08:

a= int(input())
b= int(input())
c= int(input())
str1= input()
str2= input()
fim= (str1*(a+b))+(str2*(b+c))
print(f'{(fim*(a+c))}')
'''
'''
#Questao 09:

str1= input()
melhor= len(str1)/1550
pior= len(str1)/1200
print(f'Pior dos casos: {pior:.3f}\nMelhor dos casos: {melhor:.3f}')
'''

#Questao 10:

F= int(input())
O= int(input())
P= int(input())
D= int(input())
print(f'{(((F+(P*2))*(O*2)*(D*4)))}')

