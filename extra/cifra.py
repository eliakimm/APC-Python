a= ('abcdefghijklmnopqrstuvwxyz')
a= a.upper()
for i in range(int(input())):
    c= 0
    fim=''
    cifra= input()
    n= int(input())
    for letra in cifra:
        c= a.find(letra)
        c= c-n
        if c > len(a):
            c= c-len(a)
        fim= fim + a[c]
    print(fim)