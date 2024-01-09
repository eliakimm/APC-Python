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
        print('A habidade do jogador deve estar entre 0 e 10')
        return False
    else:
        return True

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
                        
        


time= [['rodry', 'atacante', 9],['cezar','goleiro',1],['vinijr','atacante',9],['caze','meia',8],['militão','defensor',3],['silva','defensor',2],['royal','defensor',4],['lodi','defensor',6],['bruno','meia',5],['jojo','meia',11],['ney','atacante',10],['pelé','atacante',10]]
esquema= [4,2,4]




