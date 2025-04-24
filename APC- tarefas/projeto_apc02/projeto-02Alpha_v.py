def analise(jogador):
    posicao= 'goleiro', 'defensor', 'meia', 'atacante'
    nome,posi,habi= jogador
    global time
    c_j1= 0
    for i in range(len(time)):
        if time[i][0] == nome:
            c_j1+= 1
    if c_j1 > 0:
        print('Jogador já está no time')
        return False 
    if posi not in posicao:
        print( 'A posição informada não existe')
        return False
    if int(habi) > 10:
        print('A habilidade do jogador deve estar entre 0 e 10')
        return False
    else:
        return True

def cortar_nome(nome):
    if len(nome) <= 8:
        return nome
    else:
        nome1= ''
        for i in range(8):
            nome1+= nome[i]
        nome= nome1
        return nome

def ordem(lista, n):
    if len(lista) == n:
        fim = [item[0] for item in lista[:n]]
        return fim
    else:
        fim = [item[0] for item in sorted(lista, key=lambda x: x[1], reverse=True)[:n]]
        return fim

def linha_campo(fim,n):    
    if n == 4:
        linha = f'|{fim[0]:^10}{fim[1]:^10}{fim[2]:^10}{fim[3]:^10}|'
        print(linha)
        print('|' + 4 * " " + 'o' + 9 * " " + 'o' + 9 * " " + 'o' + 9 * " " + 'o' + 5 * " " + '|')
    elif n == 3:
        linha = f'|{fim[0]:^13}{fim[1]:^13}{fim[2]:^13} |'
        print(linha)
        print('|' + 5 * " " + 'o' + 12 * " " + 'o' + 12 * " " + 'o' + 8 * " " + '|')
    elif n == 2:
        linha = f'|{fim[0]:^20}{fim[1]:^20}|'
        print(linha)
        print('|' + 9 * " " + 'o' + 19 * " " + 'o' + 10 * " " + '|')


def montar_time(lista):
    global esquema
    n1,n2,n3= esquema
    po= {'goleiro': 0, 'defensor': 0, 'meia': 0, 'atacante': 0}
    banco= {'goleiro': [], 'defensor': [], 'meia': [], 'atacante': []}
    for i in range(len(lista)):
        for jgd in lista[i]:
            if jgd in po:
                po[jgd]+=1
                banco[jgd].append([lista[i][0],lista[i][2]])
    if po['goleiro'] == 0 or po['defensor'] < n1 or po['meia'] < n2 or po['atacante'] < n3:
        print('Estão faltando jogadores no time:')
        if po['goleiro'] == 0:
            print(f'1 goleiro')
        if po['defensor'] < n1:
            print(n1 - po['defensor'],'defensores')
        if po['meia'] < n2:
            print(n2 - po['meia'], 'meias')
        if po['atacante'] < n3:
            print(n3 - po['atacante'], 'atacantes')
    else:
        print('+----------------------------------------+')
        print('|              |          |              |')
        print('|               ----------               |')
        print('|                                        |')
        ata= ordem(banco['atacante'],n3)
        linha_campo(ata,n3)
        print('|                                        |')
        mei= ordem(banco['meia'],n2)
        linha_campo(mei,n2)
        print('|                  (  )                  |')
        print('|                                        |')
        print('|                                        |')
        dfs= ordem(banco['defensor'],n1)
        linha_campo(dfs,n1)
        print('|                                        |')
        print('|               ----o-----               |')
        golr= ordem(banco['goleiro'],1)
        linha= '|'+' '*14+f'|{golr[0]:^10}|'+14*' '+'|'
        print(linha)
        print('+----------------------------------------+')

time= []
n1,n2,n3= 0,0,0

while True:
    n= int(input())
    #CONTRATAR JOGADOR:
    if n == 1:
        posic= ('goleiro','defensor','meia','atacante')
        jogador_contratado= input().lower()
        jogador_contratado= list(jogador_contratado.split())
        nome,posi,habi= jogador_contratado
        habi= int(habi)
        nome= cortar_nome(nome)
        c_j1= 0
        if analise([nome,posi,habi]) == False:
            continue 
        time.append([nome,posi,habi])
    #TROCAR JOGADOR:
    elif n == 2:
        j1,j2= input().split(' x ')
        j1= list(j1.split())
        j1[0]= cortar_nome(j1[0])
        j1[2]= int(j1[2])
        j2= list(j2.split())
        j2[0]= cortar_nome(j2[0])
        j2[2]= int(j2[2])
        if analise(j2) == False:
            continue
        c_j1= 0
        c_j2= 0
        for i in range(len(time)):
            if time[i] == j1:
                c_j1+= 1
        if c_j1 == 0:
            print('Jogador não está no time')
            continue
        else:
            for k in range(len(time)):
                if time[k] == j1:
                    time[k]= j2
    #DEFINIR ESQUEMA TÁTICO:
    elif n == 3:
        n1,n2,n3= map(int,input().split())
        if n1+n2+n3 != 10:
            print('A soma das posições deve totalizar 10 jogadores')
            n1,n2,n3= 0,0,0
            continue
        if 2 <= n1 <= 4 and 2 <= n2 <= 4 and 2 <= n3 <= 4:
            continue
        else:
            print('Cada posição deve conter entre 2 e 4 jogadores')
            n1,n2,n3= 0,0,0
    #MONTAR TIME:
    elif n == 4:
        esquema= [n1,n2,n3]
        if sum(esquema) == 0:
            print('O Esquema tático deve ser estabelecido antes de montar o time')
            continue
        montar_time(time)
    #ENCERRAR LOOP:   
    elif n == 5:
        break