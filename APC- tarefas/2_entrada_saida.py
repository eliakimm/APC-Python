'''
#Questao 01:

x= input()
print(f'{x}\n{x*2}\n{x} {x}\n2{x}\n[{x}]')
'''
'''
#Questao 02:

a= input()
b= input()
c= input()

print(f'{a+b+c}\n{a}\n{b*2}\n{c} {c} {c}')
print(f'X == {a}, Y == {b}, Z == {c}')
print(f'X != {b}, Y != {a}, Z == {c}')
'''
'''
#Questao 03:

linha1= input().split()
linha2= input().split(',')
linha3= input()
print(f'Sorvete de {linha1[0]}, {linha1[1]} e {linha1[2]} com coberturas de {linha2[0]} e {linha2[1]} e calda de {linha3}!\nNão esqueça a banana!')
'''
'''
#Questao 04:

h, m, s= map(int, input().split(':'))
print(f'La se foram {(h*3600)+(m*60)+s} segundos que nao voltam mais...')
'''
'''
#Questao 05:

d, m, a= input().split('/')
print(f'{d}-{m}-{a}')
print(f'{m}-{d}-{a}')
print(f'{a}/{m}/{d}')
'''
'''
#Questao 06:

n= float(input())
print(f'{n:.4f}\n{n:.2f}\n{n:.0f}')
'''
'''
#Questao 07:

n1= (input())
n2= (input())
print(f'I1 = {n1}, I2 = {n2}')
print(f'I1 = {n1:<10}, I2 = {n2}')
print(f'I1 = {n1}, I2 = {n2:>5}')
print(f'I1 = {n1:<10}, I2 = {n2.zfill(4)}')
print(f'I1 = {n1.zfill(6)}, I2 = {n2.zfill(4)}')
'''

#Questao 08:

f1, f2= map(float, input().split())
d1, d2= map(float, input().split())
print(f'F1 = {f1}, F2 = {f2}\nD1 = {d1}, D2 = {d2}\n')
print(f'F1 = {f1:.2f}, F2 = {f2:.2f}\nD1 = {d1:.2f}, D2 = {d2:.2f}\n')
print(f'F1 = {f1:.5f}, F2 = {f2:.5f}\nD1 = {d1:.5f}, D2 = {d2:.5f}\n')
print(f'F1 = {f1:.10f}, F2 = {f2:.10f}\nD1 = {d1:.10f}, D2 = {d2:.10f}\n')
print(f'F1 = {f1:.28f}, F2 = {f2:.28f}\nD1 = {d1:.28f}, D2 = {d2:.28f}\n')
print(f'F1 = {f1:.3E}, F2 = {f2:.3E}\nD1 = {d1:.3E}, D2 = {d2:.3E}\n')
print(f'F1 = {f1:.0f}, F2 = {f2:.0f}\nD1 = {d1:.0f}, D2 = {d2:.0f}')

