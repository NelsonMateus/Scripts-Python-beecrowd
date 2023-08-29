x = int(input())
y = int(input())

#aqui o problema é que o usuário pode digitar
#tanto um número maior como primeira opção ou menor
#então temos que resolver isso no código
soma = 0 
if x < y: 
    menor = x 
    maior = y
else: 
    menor = y 
    maior = x 
for i in range(menor+1, maior):
    if i % 2 !=0: 
        soma+=i
print(soma)
