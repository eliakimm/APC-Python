"""
#01:

def achar(frase):
    letras= {'d': 0, 't': 0, 'v': 0}
    for cont in frase:
        if cont in letras:
            letras[cont]+= 1
    sequencia= (letras.items())
    for cont, quant in sequencia:
        if quant > 0:
            print(cont, quant)
frase= input()
achar(frase)
"""

"""
#02:

num = int(input())
dic= dict()
lista= []
for i in range(num):
    aluno= input().split(',')
    nota= float(aluno[1])
    dic[aluno[0]]= nota
na= float(input())
for alunos, notas in dic.items():
    if notas == na:
        lista.append(alunos)
if len(lista) > 0:
    print('/'.join(sorted(lista)))
else:
    print('Você foi o único aluno com essa nota.')
"""

"""
#03:

prod_preco = input().split()
pedido = input().split()
dic_prod = {}
dic_ped = {}
preco_total = 0

for i in range(0, len(prod_preco), 2):
    prod = prod_preco[i]
    preco = float(prod_preco[i+1])
    dic_prod[prod] = preco

for i in range(0, len(pedido), 2):
    prod = pedido[i]
    quant = float(pedido[i+1])
    dic_ped[prod] = quant

for produto, quantidade in dic_ped.items():
    if produto in dic_prod:
        preco = dic_prod[produto]
        preco_total += preco * quantidade

print(f'R$ {preco_total:.2f}')
"""
"""
#04:

turma= {}

for _ in range(int(input())):
    nome,email,n1,n2,n3,n4= input().split()
    nota= [n1,n2,n3,n4]
    nota= map(float,nota)
    turma[nome]= [email,sum(nota)/4]

aluno= input()


if aluno in turma:
    email,media= turma[aluno]
    print(f'Destinatário: {email}')
    if media >= 5:
        print(f'O aluno {aluno} foi aprovado com média {media:.2f}.')
    else:
        print(f'O aluno {aluno} foi reprovado com média {media:.2f}.')

else:
    print(f'O aluno {aluno} não está na turma.')

"""
#05:

corredor = {}
cont = 0
itens = []
soma_precos = 0

for _ in range(int(input())):
    cont += 1
    produtos = input().split()
    corredor[cont] = produtos

n = int(input())

if n in corredor:
    itens = corredor[n][::2]  

    precos = corredor[n][1::2]  
    for preco in precos:
        soma_precos += float(preco)

    preco_medio = soma_precos / len(itens) if len(itens) > 0 else 0

    print(f"No corredor {n} encontramos:")
    print(", ".join(itens))
    print(f"E o preço médio é {preco_medio:.2f}.")
else:
    print('Esse corredor não existe no mercado.')
