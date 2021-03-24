
no_case = int(input())
team = []
match = []
global a, b, c, d, e, f, g, h, I
a, b, c, d, e, f, g, h, I = dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict()
world_cup = input()
no_of_teams = int(input())


def result(res):
    for i in range(0, len(res)):
        if (res[i] == '#'):
            index = i
            break
    team_1 = res[:index]
    team_1_goals = int(res[index + 1])
    team_2_goals = int(res[index + 3])
    team_2 = res[index + 5:]

    if (team_1_goals > team_2_goals):
        d[team_1] += 1
        f[team_2] += 1
        b[team_1] += 3
    elif (team_1_goals == team_2_goals):
        e[team_1] += 1
        e[team_2] += 1
        b[team_1] += 1
        b[team_2] += 1
    else:
        d[team_2] += 1
        f[team_1] += 1
        b[team_2] += 3

    h[team_1] += team_1_goals
    I[team_1] += team_2_goals
    h[team_2] += team_2_goals
    I[team_2] += team_1_goals

    c[team_1] += 1
    c[team_2] += 1


def get_score(team):
    for i in team:
        g[i] = abs(h[i] - I[i])


for i in range(0, no_of_teams):
    t = input()
    team.append(t)
    a[t] = 0
    b[t] = 0
    c[t] = 0
    d[t] = 0
    e[t] = 0
    f[t] = 0
    g[t] = 0
    h[t] = 0
    I[t] = 0

no_of_matches = int(input())

for i in range(0, no_of_matches):
    match.append(input())

for i in range(0, no_of_matches):
    result(match[i])

get_score(team)

for i in team:
    print(i, b[i], c[i], "g (", d[i], '-', e[i], '-', abs(f[i]), ")", g[i], "gd (", h[i], "-", I[i], ")")

