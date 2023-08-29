N1, N2, N3, N4 = input().split(" ")

p1 = 2
p2 = 3
p3 = 4 
p4 = 1 

med = float(N1)*float(p1) + float(N2)*float(p2) + float(N3)*float(p3) + float(N4)*float(p4)
media = med / (float(p1) + float(p2) + float(p3) + float(p4))
if media < 5: 
    print("Media:%0.1f"%media) 
    print("Aluno reprovado.")
elif 5 <= media <= 6.9: 
    print("Media:%0.1f"%media) 
    print('Aluno em exame')
    n = float(input())
    print("Nota do exame:%0.1f"%n)
    pontuacao= (n + media)/2
    if pontuacao >=5.0:
        print("Aluno aprovado")
        print(" Media Final: %0.1f"%pontuacao)
    else:
        print("Aluno reprovado")
        print(" Nota do exame:%0.1f"%pontuacao)
if media >= 7:
    print("Aluno aprovado.")
    print("Media Final: %0.1f"%media)

