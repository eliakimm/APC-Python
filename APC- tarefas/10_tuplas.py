"""
#01:

def tuplaDupla(n1,n2):
    return (n1,n2)
    
"""
""""
#02:

def convert(lista):
    dic= {}
    for chave, valor in lista:
        if chave in dic:
            dic[chave].append(valor)
        else:
            dic[chave]= [valor]
    return dic

"""
"""
#03:

l1= []
l2= []
media= []
duplas= []
for i in range(10):
    if i < 5:
        l1.append(int(input()))
    else:
        l2.append(int(input()))
lista_tuplas= zip(l1, l2)
for a, b in lista_tuplas:
    duplas.append((a,b))
    md= (a+b)/2
    media.append(md)
print(duplas)
print(media)
"""
"""
#04:

def erase(lista):
    fim= []
    for i in lista:
        if len(i) > 0:
            fim.append((i))
    return fim
l = [(0), (10, 0), (0, 0)]
resposta = erase(l)
print(resposta)
"""
#05:

def stockmarket(lista):
    compras= {}
    for data, preco, quant, _ in lista:
        total= float(preco * quant)
        if data in compras:
            compras[data]+= total
        else:
            compras[data]= total
    return compras
stock = [('25-Out-2020', 37.58, 100, 'GM'),
('25-Out-2020', 37.58, 100, 'FIT'),
('25-Out-2020', 37.58, 100, 'FRD'),
('25-Out-2020', 37.58, 100, 'HND'),
('25-Out-2020', 37.58, 100, 'TYO'),
('25-Out-2020', 37.58, 100, 'CHV'),
('25-Out-2020', 37.58, 100, 'JEP')]
print(stockmarket(stock)) 
    


