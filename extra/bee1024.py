for i in range(int(input())):
    code= input()
    pass1= ''
    pass2= ''
    pass3= ''
    for i in code:
        if i.isalpha():
            c= ord(i) +3
            pass1= pass1 + chr(c)
        else:
            pass1= pass1 + i
    pass2= pass1[::-1]
    meio= len(pass2)//2
    for i in pass2[meio:]:
        c= ord(i) -1
        pass3= pass3 + chr(c)
    pass3= pass2[:meio] + pass3
    print(pass3)
