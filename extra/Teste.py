i = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']

n1 = input()
palavras = n1.split()
n2= ''

for palavra in palavras:
    if palavra in i:
        num = str(i.index(palavra))
        n2 += num + ' '
    else:
        n2 += palavra + ' '

print(n2.strip())