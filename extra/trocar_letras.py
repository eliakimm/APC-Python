import random

palavra= input()

novo= ''
n= range(len(palavra))
verif= list(n)

for i in range(len(palavra)):
    if len(verif) == 0:
        break
    numero= random.choice(verif)
    verif.remove(numero)
    novo= novo + palavra[numero]

print('-'*20)
print(f'|{novo:^20}|')
print('-'*20)