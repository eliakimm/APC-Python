num= int(input())
lista= []
for n in range(num+1):
    nomes= input()
    lista.append(nomes)
sus= lista[-1].split()
novo= []
for i in lista[:-1]:
    if i not in sus:
        novo.append(i)
print(*novo)
    