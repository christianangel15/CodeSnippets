def numberOfTokens(expiryLimit, commands):
    save = []
    comm = commands
    n = len(comm)
    for i in range(n):
        if (comm[i][0] == 0):
            comm[i][2] = comm[i][2] + expiryLimit
            token = [comm[i][0], comm[i][1], comm[i][2]]
            save.append(token)

        if (comm[i][0] == 1):
            for j in range(len(save)):
                if (comm[i][1] == save[j][1] and comm[i][2] > save[j][2]):
                    save.pop(j)

                elif (comm[i][1] == save[j][1] and comm[i][2] == save[j][2]):
                    save[j][2] = save[j][2] + expiryLimit
    print(len(save))
numberOfTokens(3, [[0,1,1],[1,1,5]])
numberOfTokens(3, [[0,1,1],[1,1,4],[1,2,5]])

