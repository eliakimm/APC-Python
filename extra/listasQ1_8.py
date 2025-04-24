def mediana_e_mais_proximo_media_e_pos(lista0):
    
    lista = lista0[:]
    lista.sort()
    tam = len(lista0)
    if tam > 0:
        if tam % 2 == 0:
            mediana = (lista[tam // 2] + lista[tam // 2 - 1]) / 2
        else:
            mediana = lista[tam // 2] 
        
        media = (sum(lista)) / tam
        
        delta = abs(lista[0] - media)
        prox_media = lista[0]
        index = 0
        for i in range(len(lista0)):
            if abs(lista0[i] - media) < delta:
                prox_media = lista0[i]
                index = i
                delta = abs(lista0[i] - media)
    else:
        mediana = None
        prox_media = None
        index = None
    
    return [mediana, prox_media, index]

lista = [1, 2, 3, 4]
print(mediana_e_mais_proximo_media_e_pos(lista))