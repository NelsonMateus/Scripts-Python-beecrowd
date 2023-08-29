valor = input().split(" ")

A,B = valor

if int(A)%int(B)==0  or int(B)%int(A)==0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")