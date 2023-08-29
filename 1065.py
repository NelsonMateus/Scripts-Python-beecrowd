contador=0
for i in range(5): 
    n = int(input())
    if n % 2 == 0: 
        contador+=1
print(contador, 'valores pares')