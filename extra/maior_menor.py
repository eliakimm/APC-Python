sm= 1000000000.00
nm= None
while True:
    n, s= input().split(',')
    s= float(s)
    if n == 'Fim':
        break
    else:
        if s < sm:
            sm= s
            nm= n

if nm is None: 
    print('Não tem')
else:
    print(nm)