import unicodedata

###REMOVER ACENTOS DAS PALAVRAS:
def remover_acentos(palavra):
    return ''.join([c for c in unicodedata.normalize('NFKD', palavra) if not unicodedata.combining(c)])

###REMOVER ASPAS SIMPLES E DUPLAS/QUEBRAR A PALAVRA:
def quebrar_palavra(frase):
    digitos= ["'", '"', "-"]
    nova_palavra= ''
    for palavra in frase:
        for letra in palavra:
            if letra in digitos:
                nova_palavra+= ' '
            else:
                nova_palavra+= letra
        nova_palavra+= ' '
    return nova_palavra.split()
        
###ENTRADA:
digitos = str.maketrans(" "," ", "$£/\´`~^.,;:!?()ª°ªº0123456789")
entrada= input()
entrada= entrada.translate(digitos)
entrada= entrada.split()
entrada= quebrar_palavra(entrada)

###PALAVRAS DISPENSAVEIS:
artigos= "o", "a", "os", "as", "aos", "um", "uma", "uns", "umas"
preposições= "da", "de", "dos", "das", "para", "com", "em", "por", "sobre", "sob", "entre", "a", "ante", "após", "até", "contra", "desde", "perante", "per", "por", "sem", "como"
pronomes= "eu", "tu", "ele", "ela", "nós", "vós", "eles", "elas", "me", "te", "se", "nos", "vos", "o", "a", "lhe", "lhes", "se", "meu", "minha", "seu", "sua", "nosso", "nossa", "vosso", "vossa"

lista_1= []###LISTA DE PALAVRAS PRINCIPAL;
lista_2= []###LISTA DE PALAVRAS IMPRIMIDAS;

###REMOVE PALAVARS DISPENSADAS:
for palavra in entrada:
    palavra_minuscula= palavra.lower()
    palavra_minuscula= remover_acentos(palavra_minuscula)
    if palavra_minuscula not in artigos and palavra_minuscula not in preposições and palavra_minuscula not in pronomes:
        lista_1.append(palavra_minuscula)

###SAIDA:
print('Frequencia de palavras do texto:')

for i in range(len(lista_1)):
    if len(lista_1[i]) >= 3:
        palavra = lista_1[i]
        c = lista_1.count(palavra)
        if (palavra, c) not in lista_2:
            print(f"'{palavra}': {c}.")
            lista_2.append((palavra, c))