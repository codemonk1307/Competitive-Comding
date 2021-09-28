
t = int(input())
for p in range(t):

    n = int(input())
    gridDominoes = str(input())
    otherhalf = [] * (n + 1)

    for i in range(n):
        if gridDominoes == "U":
            otherhalf.append("D")

        elif gridDominoes == "D":
            otherhalf.append("U")
            
        elif gridDominoes[i] == "L" or gridDominoes[i] == "R":
            otherhalf.append(gridDominoes[i])

    print("".join(otherhalf))

