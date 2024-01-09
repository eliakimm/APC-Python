#01:

# def virgula(f):
#     if ',' in f:
#         print('passed')
#     else:
#         print('failed')
# f= input()
# virgula(f)

#02:

# f= input()
# print(f'{f[:2]}{f[-2:]}')

#03:

# frase= input()
# c= 0
# for i in frase:
#     if i.isdigit():
#         c+=1
# print(c)

#04:

# frase= input()
# print(frase[1::2].replace(' ',''))

#05:

# frase= input()
# frase= frase.replace('zero','0')
# frase= frase.replace('um','1')
# frase= frase.replace('dois','2')
# frase= frase.replace('três','3')
# frase= frase.replace('quatro','4')
# frase= frase.replace('cinco','5')
# frase= frase.replace('seis','6')
# frase= frase.replace('sete','7')
# frase= frase.replace('oito','8')
# frase= frase.replace('nove','9')
# print(frase)

#06:

# frase= input()
# palavra= input()
# if palavra in frase:
#     frase= frase.replace(palavra, '*')
#     print(frase)
# else:
#     print('tudo certo :)')


#07:

# palavra= input()
# lista1= list(palavra)
# c= 0
# for i in range(len(palavra)//2):
#     if lista1[i] != lista1[-(i+1)]:
#         c+= 1
#         lista1[i] = lista1[-(i + 1)] = max(lista1[i], lista1[-(i + 1)])
# if c == 1 or (c == 0 and len(palavra) % 2 == 1):
#     print('ON')
# else:
#     print('OFF')

#08:

# for i in range(int(input())):
#     palavra= input()
#     nova_str= ''
#     letra= ''
#     for item in palavra:
#         if item.isalpha():
#             letra+= ' ' + item + ' '
#         if item.isdigit():
#             letra+=  item
#     letra= letra.split()
#     for i in range(len(letra)):
#         if letra[i].isalpha():
#             l= ''
#             l= letra[i]
#         if letra[i].isdigit():
#             nova_str+=  l * int(letra[i])
#     print(nova_str)

#09:

def não_possui_a_letra_u(palavra):
    palavra= palavra.lower()
    u= 'u ú ù ü û'
    for i in range(len(palavra)):
        if palavra[i] in u:
            return False
    return True

print(não_possui_a_letra_u("manu"))



