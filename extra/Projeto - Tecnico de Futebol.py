et = []

posições = 'goleiro','defensor','meia','atacante'

clube = {}
gol = []
defe = []
mei = []
ata = []

def montartime (et,formacao):
    for i, escalacao in enumerate(et):
                if i == 0:
                    for index, qtd in enumerate(escalacao):
                        if index == 0:
                            for i in range(0, qtd):
                              formacao[0].append(defe[i][0])

                        if index == 1:
                            for i in range(0, qtd):
                              formacao[1].append(mei[i][0])
                        
                        if index == 2:
                            for i in range(0, qtd):
                              formacao[2].append(ata[i][0])


while(1):
    linha = int(input())
    if linha == 1:
        entrada = input().split()
        if len(entrada) == 3:
            nome1 = entrada[0]
            pos = entrada[1]
            hab = entrada[2]
            if nome1.isalpha() == True:
                if len(nome1) > 8:
                    nome = nome1[:8]
                    if nome.lower() not in clube:
                        if pos in posições:
                            if 0 <= int(hab) <=10:
                                clube[nome.lower()] = [nome.lower(),pos,int(hab)]
                            else:
                                print('A habilidade do jogador deve estar entre 0 e 10')
                        else:
                            print('A posição informada não existe')
                    else:
                        print('Jogador já está no time')
                else:
                    if nome1.lower() not in clube:
                        if pos in posições:
                            if 0 <= int(hab) <=10:
                                clube[nome1.lower()] = [nome1.lower(),pos,int(hab)]
                            else:
                                print('A habilidade do jogador deve estar entre 0 e 10')
                        else:
                            print('A posição informada não existe')
                    else:
                        print('Jogador já está no time')
        
    elif linha == 2:
        entrada1 = input().split(' x ')
        jogador1 = entrada1[0].split()
        jogador2 = entrada1[1].split()
        
        if len(jogador1) == 3:
            nome1 = jogador1[0]
            pos = jogador1[1]
            hab = jogador1[2]
            if nome1.isalpha() == True:
                if len(nome1) > 8:
                    nome = nome1[:8]
                    if nome.lower() in clube:
                        if pos in posições:
                            if 0 <= int(hab) <=10:
                                if len(jogador2) == 3:
                                    nome3 = jogador2[0]
                                    pos = jogador2[1]
                                    hab = jogador2[2]
                                    if nome3.isalpha() == True:
                                        
                                        if len(nome3) > 8:
                                            nome5 = nome3[:8]                                    
                                            if nome5.lower() not in clube:
                                                if pos in posições:
                                                    if 0 <= int(hab) <=10:
                                                        del clube[nome.lower()]
                                                        clube[nome5.lower()] = [nome5.lower(),pos,int(hab)]
                                
                                                    else:
                                                        print('A habilidade do jogador deve estar entre 0 e 10')
                                                else:
                                                    print('A posição informada não existe')
                                            else:
                                                print('Jogador já está no time')
                                        else:
                                            if nome3.lower() not in clube:
                                                if pos in posições:
                                                    if 0 <= int(hab) <=10:
                                                        del clube[nome.lower()]
                                                        clube[nome3.lower()]=[nome3.lower(),pos,int(hab)]
                                
                                                    else:
                                                        print('A habilidade do jogador deve estar entre 0 e 10')
                                                else:
                                                    print('A posição informada não existe')
                                            else:
                                                print('Jogador já está no time')
                            else:
                                print('Jogador não está no time')
                        else:
                            print('Jogador não está no time')
                    else:
                        print('Jogador não está no time')
                else:
                    if nome1.lower() in clube:
                        if pos in posições:
                            if 0 <= int(hab) <=10:
                                if len(jogador2) == 3:
                                    nome3 = jogador2[0]
                                    pos = jogador2[1]
                                    hab = jogador2[2]
                                    if nome3.isalpha() == True:
                                        
                                        if len(nome3) > 8:
                                            nome5 = nome3[:8]                                    
                                            if nome5.lower() not in clube:
                                                if pos in posições:
                                                    if 0 <= int(hab) <=10:
                                                        del clube[nome.lower()]
                                                        clube[nome5.lower()]=[nome5.lower(),pos,int(hab)]
                                
                                                    else:
                                                        print('A habilidade do jogador deve estar entre 0 e 10')
                                                else:
                                                    print('A posição informada não existe')
                                            else:
                                                print('Jogador já está no time')
                                        else:
                                            if nome3.lower() not in clube:
                                                if pos in posições:
                                                    if 0 <= int(hab) <=10:
                                                        del clube[nome3.lower()]
                                                        clube[nome3.lower()]=[nome3.lower(),pos,int(hab)]
                                
                                                    else:
                                                        print('A habilidade do jogador deve estar entre 0 e 10')
                                                else:
                                                    print('A posição informada não existe')
                                            else:
                                                print('Jogador já está no time')
                            else:
                                print('Jogador não está no time')
                        else:
                            print('Jogador não está no time')
                    else:
                        print('Jogador não está no time')
            else:
                print('Jogador não está no time')
      
    elif linha == 3:
        qd,qm,qat = map(int,input().split())
        if (qd+qm+qat) == 10:
            if 4>= qd >=2:
                if 4>= qm >=2:
                    if 4>= qat >=2:
                        et.append([qd,qm,qat])
                    else:
                        print('Cada posição deve conter entre 2 e 4 jogadores')
                else:
                    print('Cada posição deve conter entre 2 e 4 jogadores')
            else:
                print('Cada posição deve conter entre 2 e 4 jogadores')
        else:
            print('A soma das posições deve totalizar 10 jogadores')
        
    elif linha == 4:
        if len(et) == 0:
            print('O Esquema tático deve ser estabelecido antes de montar o time')
        
        elif len(clube) < 10:
            print('Estão faltando jogadores no time:')
            if len(gol) == 0:
                print('1 goleiro')
            
            if len(defe) == 0:
                print('3 defensores')
            elif len(defe) == 1:
                print('2 defensores')
            elif len(defe) == 2:
                print('1 defensores')
            
            if len(mei) == 0:
                print('3 meias')
            elif len(mei) == 1:
                print('2 meias')
            elif len(mei) == 2:
                print('1 meias')
            
            if len(ata) == 0:
                print('3 atacantes')
            elif len(ata) == 1:
                print('2 atacantes')
            elif len(ata) == 2:
                print('1 atacantes')
        
        elif len(defe)+len(mei)+len(ata) == 0:
            for chave, l in clube.items():
                if len(gol) != 1 and 'goleiro' in l:
                    gol.append(clube[chave])
                elif len(ata) < 3 or len(ata) >= 3 and 'atacante' in l:
                    ata.append(clube[chave])
                    ata.sort(key=lambda x: x[2], reverse=True)
                    ata = [item[:3] for item in ata]
                elif len(defe) < 3 or len(defe) >= 3 and 'defensor' in l:
                    defe.append(clube[chave])
                    defe.sort(key=lambda x: x[2], reverse=True)
                    defe = [item[:3] for item in defe]
                elif len(mei) < 3 or len(mei) >= 3 and 'meia' in l:
                    mei.append(clube[chave])
                    mei.sort(key=lambda x: x[2], reverse=True)
                    mei = [item[:3] for item in mei]
            
        if len(defe)+len(mei)+len(ata) >= 10:
            formacao = [[], [], []]
            montartime(et,formacao)
            del et[0]
                                                         
                        
            print('+----------------------------------------+')
            print('|              |          |              |')
            print('|               ----------               |')
            print('|                                        |')
            if len(formacao[2]) == 2:
                print(f"|{formacao[2][0]:^20}{formacao[2][1]:^20}|")
                print('|' + 9 * " " + 'o' + 19 * " " + 'o' + 10 * " " + '|')
            elif len(formacao[2]) == 3: 
                print(f"|{formacao[2][0]:^13}{formacao[2][1]:^13}{formacao[2][2]:^13} |")
                print('|' + 5 * " " + 'o' + 12 * " " + 'o' + 12 * " " + 'o' + 8 * " " + '|')
            elif len(formacao[2]) ==4:
                print(f"|{formacao[2][0]:^10}{formacao[2][1]:^10}{formacao[2][2]:^10}{formacao[2][3]:^10}|")
                print('|' + 4 * " " + 'o' + 9 * " " + 'o' + 9 * " " + 'o' + 9 * " " + 'o' + 5 * " " + '|')
            print('|                                        |')
            if len(formacao[1]) == 2:
                print(f"|{formacao[1][0]:^20}{formacao[1][1]:^20}|")
                print('|' + 9 * " " + 'o' + 19 * " " + 'o' + 10 * " " + '|')
            elif len(formacao[1]) == 3:
                print(f"|{formacao[1][0]:^13}{formacao[1][1]:^13}{formacao[1][2]:^13} |")
                print('|' + 5 * " " + 'o' + 12 * " " + 'o' + 12 * " " + 'o' + 8 * " " + '|')
            elif len(formacao[1]) ==4:
                print(f"|{formacao[1][0]:^10}{formacao[1][1]:^10}{formacao[1][2]:^10}{formacao[1][3]:^10}|")
                print('|' + 4 * " " + 'o' + 9 * " " + 'o' + 9 * " " + 'o' + 9 * " " + 'o' + 5 * " " + '|')
            print('|                  (  )                  |')
            print('|                                        |')
            print('|                                        |')
            if len(formacao[0]) == 2:
                print(f"|{formacao[0][0]:^20}{formacao[0][1]:^20}|")
                print('|' + 9 * " " + 'o' + 19 * " " + 'o' + 10 * " " + '|')
            elif len(formacao[0]) == 3:
                print(f"|{formacao[0][0]:^13}{formacao[0][1]:^13}{formacao[0][2]:^13} |")
                print('|' + 5 * " " + 'o' + 12 * " " + 'o' + 12 * " " + 'o' + 8 * " " + '|')
            elif len(formacao[0]) == 4:
                print(f"|{formacao[0][0]:^10}{formacao[0][1]:^10}{formacao[0][2]:^10}{formacao[0][3]:^10}|")
                print('|' + 4 * " " + 'o' + 9 * " " + 'o' + 9 * " " + 'o' + 9 * " " + 'o' + 5 * " " + '|')
            print('|                                        |')
            print('|               ----o-----               |')
            linha= '|'+' '*14+f'|{gol[0][0]:^10}|'+14*' '+'|'
            print(linha)
            print('+----------------------------------------+')   
        
    elif linha == 5:
        break