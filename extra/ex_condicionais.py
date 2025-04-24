p1=input('O programa funciona?\n')
if p1 == 'SIM':
    p2=input('Você entende o que fez?\n')
    if p2 == 'SIM':
        print('Ótimo. Então não mexe!\n')
    elif p2 == 'NÃO':
        p3= input('Já foi na tutoria?\n')
        if p3 == 'SIM':
            print('Choremos!\n')
        elif p3 == 'NÃO':
            print('Temos um time a disposição!\n')
elif p1 == 'NÃO':
    p4=input('Você sabe onde está o erro?\n')
    if p4 == 'SIM':
        p5= input('Acha que pode solucionar sozinho?\n')
        if p5 == 'SIM':
            print('Então mão na massa!\n')
        elif p5 == 'NÃO':
            p6= input('Já pesquisou no Google?\n')
            if p6 == 'SIM':
                p7= input('Já foi na tutoria?\n')
                if p7 == 'SIM':
                    print('Choremos!\n')
                elif p7 == 'NÃO':
                    print('Temos um time a disposição!\n')
            elif p6 == 'NÃO':
                print('Corre lá então\n')
    elif p4 == 'NÃO':
        p8= input('Já foi na tutoria?\n')
        if p8 == 'SIM':
            print('Choremos!\n')
        elif p8 == 'NÃO':
            print('Temos um time a disposição!\n') 