cand_name = []
vote_list = []
result = []
result_low = []
winner = []
cases = int(input("Enter the number of Cases: "))
for x in range(0,cases):
    print('')
    parti = int(input("Enter the number of Candidates: "))
    for i in range(1,parti+1):
        cand_name.append(input("Enter the name of candidate "+str(i)+" : "))
        result.append(0)
        result_low.append(0)
    voters = int(input("Enter the number of Voters: "))
    for i in range(0,voters):
        vote_list.append(input().split())
    controler = 0
    while(controler < int(parti)):
        for j in range(0,voters):
            for i in range(1,parti+1):
                if int(vote_list[j][controler]) == i:
                    result[(i-1)] = int(result[(i-1)]) + 1
                if int(vote_list[j][(parti-1)]) == i:
                    result_low[(i-1)] = int(result_low[(i-1)]) + 1
        for i in range(0,parti):
            if result[i] >= (voters/2):
                winner.append(cand_name[i])
            result[i] = 0
        if winner:
            print(winner)
            exit(0)
        cand_name.pop(result_low.index(max(result_low)))
        sw = (result_low.index(max(result_low)))+1
        for i in range(0,voters):
            for j in range(0,parti-1):
                if int(vote_list[i][j]) == int(sw):
                    vote_list[i][j] = vote_list[i][j+1]
        parti -= 1
        controler += 1
    print("master Failure")
