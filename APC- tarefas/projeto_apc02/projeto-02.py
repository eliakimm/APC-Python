#CONTRATAR JOGADOR: 1
def contratar(lista1, lista2):
    posicao= 'goleiro', 'defensor', 'meia', 'atacante'
    nome1= ''
    jogador= input().lower()
    nome,posi,habi= jogador.split()
    if len(nome) > 8:
        for i in range(8):
            nome1+= nome[i]
        nome= nome1
    if posi not in posicao:
        print( 'A posição informada não existe')
        return lista1, lista2
    if int(habi) > 10:
        print('A habidade do jogador deve estar entre 0 e 10')
        return lista1, lista2
    if nome in lista2:
        print ('Jogador já está no time')
        return lista1, lista2
    else:
        lista1.append(jogador)
        lista2.append(nome)
    return lista1, lista2

#TROCAR JOGADOR: 2
def trocar(lista1,lista2):
    j1,j2= input().lower().split(' x ')
    n1,p1,h1= j1.split()
    n2,p2,h2= j2.split()
    posicao= 'goleiro', 'defensor', 'meia', 'atacante'
    nome1= ''
    if len(j1[0]) > 8:
        for i in range(8):
            nome1+= nome[i]
        j1[0]= nome1[:]
        nome1= ''
    if len(j2[0]) > 8:
        for i in range(8):
            nome1+= nome[i]
        j2[0]= nome1[:]
        nome1= ''
    if p2 not in posicao:
        print( 'A posição informada não existe')
        return lista1, lista2
    if int(h2) > 10:
        print('A habidade do jogador deve estar entre 0 e 10')
        return lista1, lista2
    if j1 not in lista1:
        print('Jogador não está no time')
        return lista1, lista2
    else:
        for j in range(len(lista1)):
            if lista1[j] == j1:
                lista1[j]= j2
        for k in range(len(lista2)):
            if lista2[k] == n1:
                lista2[k]= n2
    return lista1, lista2, j1[0]

#POSIÇÃO DO JOGADOR:
def posicao(lista1,lista2):
    ata= []
    defe= []
    meias= []
    gol= []
    jogador= ''
    dic= {'goleiro': 0,'defensor': 0, 'meia': 0, 'atacante': 0}
    for i in range(len(lista1)):
        jogador= lista1[i].split()
        if 'goleiro'in jogador[1]:
            dic['goleiro']+= 1
            gol.append((jogador[0],int(jogador[2])))
        elif 'defensor' in jogador[1]:
            dic['defensor']+= 1
            defe.append((jogador[0],int(jogador[2])))
        elif 'meia' in jogador[1]:
            dic['meia']+= 1
            meias.append((jogador[0],int(jogador[2])))
        elif 'atacante' in jogador[1]:
            dic['atacante']+= 1
            ata.append((jogador[0],int(jogador[2])))
    return gol,defe,meias,ata

#REMOVER JOGADOR:
def remover(gol, defe, meias, ata,j1):
    for i in gol:
        if j1 in i:
            gol.remove(i)
    for j in gol:
        if j1 in j:
            defe.remove(j)
    for k in gol:
        if j1 in k:
            meias.remove(k)
    for m in gol:
        if j1 in m:
            ata.remove(m)
    return gol, defe, meias, ata

#MONTAR TIME: 4
def montar_time(l1, l2, l3, l4, l5):
    if sum(l5) == 0:
        print('O Esquema tático deve ser estabelecido antes de montar o time')
        return ''
    if len(l1) == 0 or len(l2) < l5[0] or len(l3) < l5[1] or len(l4) < l5[2]:
        print('Estão faltando jogadores no time:')
        if len(l1) - 1 <= 0:
            print(f'1 goleiro')
        if len(l2) < l5[0]:
            print(f'{l5[0] - len(l2)} defensores')
        if len(l3) < l5[1]:
            print(f'{l5[1] - len(l3)} meias')
        if len(l4) < l5[2]:
            print(f'{l5[2] - len(l4)} atacantes')
    return ''
    
#ENTRADA:
n = int(input())
time = []
jogadores = []
l = [0, 0, 0]
gol, defe, meias, ata = [],[],[],[]
j_removido= ''

while n != 5:
    if n == 1:
        time,jogadores= contratar(time, jogadores)
        gol, defe, meias, ata= posicao(time,jogadores)
    elif n == 2:
        time,jogadores,j_removido= trocar(time, jogadores)
        remover(gol, defe, meias, ata)
    elif n == 3:
        n1, n2, n3 = map(int, input().split())
        if n1 + n2 + n3 == 10:
            if 2 <= n1 <= 4 and 2 <= n2 <= 4 and 2 <= n3 <= 4:
                l = [n1, n2, n3]
            else:
                print('Cada posição deve conter entre 2 e 4 jogadores')
                n1, n2, n3 = 0, 0, 0
        else:
            print('A soma das posições deve totalizar 10 jogadores')
            n1, n2, n3 = 0, 0, 0
    elif n == 4:
        montar_time(gol, defe, meias, ata, l)
    n = int(input())
    
    