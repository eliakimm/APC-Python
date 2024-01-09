def remover_digito(palavra):
    digitos= ['°','ª','º','0','1','2','3','4','5','6','7','8','9']
    nova_palavra = ''.join([letra for letra in palavra if letra not in digitos])
    return nova_palavra