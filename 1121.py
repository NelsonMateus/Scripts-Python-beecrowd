N, M = map(int, input().split())
arena = [input() for _ in range(N)]

pos_i, pos_j, orient = input().split()

moves = input()

figurinhas_coletadas = 0

for move in moves:
    if move == 'D':
        if orient == 'N':
            orient = 'L'
        elif orient == 'L':
            orient = 'S'
        elif orient == 'S':
            orient = 'O'
        else:
            orient = 'N'
    elif move == 'E':
        if orient == 'N':
            orient = 'O'
        elif orient == 'O':
            orient = 'S'
        elif orient == 'S':
            orient = 'L'
        else:
            orient = 'N'
    else:
        if orient == 'N':
            if pos_i > 0 and arena[pos_i-1][pos_j] != '#':
                pos_i -= 1
                if arena[pos_i][pos_j] == '*':
                    figurinhas_coletadas += 1
        elif orient == 'L':
            if pos_j < M-1 and arena[pos_i][pos_j+1] != '#':
                pos_j += 1
                if arena[pos_i][pos_j] == '*':
                    figurinhas_coletadas += 1
        elif orient == 'S':
            if pos_i < N-1 and arena[pos_i+1][pos_j] != '#':
                pos_i += 1
                if arena[pos_i][pos_j] == '*':
                    figurinhas_coletadas += 1
        else:
            if pos_j > 0 and arena[pos_i][pos_j-1] != '#':
                pos_j -=1
