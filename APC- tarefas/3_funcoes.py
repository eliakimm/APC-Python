'''
#Questao 01:

def fahrenheit(c):
    print(f'Fahrenheit: {(1.8*c)+32:.2f}')

def kelvin(c):
    print(f'Kelvin: {c+273.15:.2f}')
'''
'''
#Questao 02:

def estilo(s, n, f):
    print(f'{s*n}{f}{s*n}')
'''
'''
#Questao 03:

def n_termo(i, r, e):
    n_esimo= i+(e-1)* r
    return n_esimo
'''
'''
#Questao 04:

def nota(n):
    print(f'|'+'★'*n+'☆'*(10-n)+'|')
'''
'''
#Questao 05:

def trocaOrdem(str1, str2):
    return (f'{str2},{str1}')
'''
'''
#Questao 06:

def areas(a, b, c):
    print(f'{a*b}\n{b*c//2}\n{((c+b)*a)//2}')
'''
'''
#Questao 07:

def distancia(x1, y1, x2, y2):
    dis= (x1-x2)**2+(((y1-y2)**2))
    return dis **0.5
'''

#Questao 08:

def estrofe(n):
    print(f'{n} patinhos\nForam passear\nAlém das montanhas\nPara brincar\nA mamãe gritou\nQuá, quá, quá, quá!\nMas só {n-1} patinhos\nVoltaram de lá')
    refrao()
def refrao():
    print('Agora só falta aprender a fazer loop!')





