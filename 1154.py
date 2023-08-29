n = int(input())
soma=0
contador=0
while n >=0:
    soma+=n
    contador+=1
    n = int(input())
if contador > 0:
    media = soma / contador
    print("%0.2f"%media)
    