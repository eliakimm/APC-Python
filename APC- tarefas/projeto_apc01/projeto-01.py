import string
import unicodedata

###REMOVER ACENTOS DAS PALAVRAS:
def remover_acentos(palavra):
    return ''.join([c for c in unicodedata.normalize('NFKD', palavra) if not unicodedata.combining(c)])

###ENTRADA:
entrada= input()
entrada= entrada.translate(str.maketrans('', '', string.punctuation))
entrada= entrada.split()

###PALAVRAS DISPENSAVEIS:
artigos= "o", "a", "os", "as", "aos", "um", "uma", "uns", "umas"
preposições= "da", "de", "dos", "das", "para", "com", "em", "por", "sobre", "sob", "entre", "a", "ante", "após", "até", "contra", "desde", "perante", "per", "por", "sem", "como"
pronomes= "eu", "tu", "ele", "ela", "nós", "vós", "eles", "elas", "me", "te", "se", "nos", "vos", "o", "a", "lhe", "lhes", "se", "meu", "minha", "seu", "sua", "nosso", "nossa", "vosso", "vossa"

lista_1= []###LISTA DE PALAVRAS PRINCIPAL;
lista_2= []###LISTA DE PALAVRAS IMPRIMIDAS;

###REMOVE PALAVARS DISPENSADAS:
for palavra in entrada:
    palavra_minuscula= remover_acentos(palavra.lower())
    if palavra_minuscula not in artigos and palavra_minuscula not in preposições and palavra_minuscula not in pronomes:
        lista_1.append(palavra_minuscula)

###SAIDA:
print('Frequencia de palavras do texto:')

for i in range(len(lista_1)):
    if len(lista_1[i]) >= 3 and lista_1[i].isdigit() == False:
        palavra = lista_1[i]
        c = lista_1.count(palavra)
        if (palavra, c) not in lista_2:
            print(f"'{palavra}': {c}.")
            lista_2.append((palavra, c))