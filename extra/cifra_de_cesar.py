def cifra(n,f):
    cifra= ''
    for i in f:
        for j in range(len(i)):
            c= ord(i[j])+(n)
            cifra= cifra + chr(c)
    print(cifra)

def decode_cifra(n,f):
    cifra= ''
    for i in f:
        for j in range(len(i)):
            c= ord(i[j])-(n)
            cifra= cifra + chr(c)
    print(cifra)