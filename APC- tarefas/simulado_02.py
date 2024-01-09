#01: 

# def remover(frase,sla):
#     nv= ''
#     if len(frase.split()) > 1:
#         for palavra in frase.split():
#             nv+= palavra.replace(sla,'').replace(sla[::-1],'')
#             nv+= ' '
#         print(nv.rstrip())
#     else:
#         print(frase.replace(sla,'').replace(sla[::-1],''))
# 
# sla= input()
# 
# while True:
#     frase= input()
#     remover(frase,sla)
#     if frase == '':
#         break
    

#02

# n= int(input())
# alarmes= []
# turmas= []
# 
# for i in range(n):
#     hora,turma= input().split()
#     turmas.append((hora,turma))
#     hora= hora.split('h')
#     alarmes.append([hora[0],hora[1]])
# 
# alarme1= ((int(alarmes[0][1])) - 55) + 60
# alarme2= ((int(alarmes[0][0])*60) - 55) //60
# alarme1= str(alarme1)
# alarme2= str(alarme2)
# print(f'{alarme2.zfill(2)}h{alarme1.zfill(2)} ALARME 1')
# cont= 1
# for j in range(2):
#     cont+=1
#     alarme1= int(alarme1) + 5
#     alarme2= int(alarme2)
#     if alarme1 == 60:
#         alarme1= 0
#         alarme2+=1
#     alarme2= ((int(alarme2)*60) + 5)//60
#     alarme1= str(alarme1)
#     alarme2= str(alarme2)
#     print(f'{alarme2.zfill(2)}h{alarme1.zfill(2)} ALARME {cont}')
# 
# for h,t in turmas:
#     print(f'{h} {t}')


#03:

# def contagem(n):
#     if n == -10:
#         print(n)
#     else:
#         contagem(n-1)
#         print(n)