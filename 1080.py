# preciso declarar um variavel que vai armazenar o maior valor 
# uma variavel que armazena a posicao 
# um loope que permite a entrada dos 100 valores 
n = int(input())
x=0
for i in range(1,100):
    a = int(input())
    if a > x:
        maior = a
        posicao = i + 1
        x = a
print(maior)
print(posicao)