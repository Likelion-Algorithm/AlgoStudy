import sys

N = int(input())
DEPTH = N // 2
G = []
min_gap = [sys.maxsize]
team_start = []
team_link = []


for m in range(N):
    G.append(sys.stdin.readline().split())


def dfs(root):
    print(team_start, team_link)
    if min_gap[0] == 0:
        return

    if root not in team_start:
        team_start.append(root)
    else:
        team_start.pop()
        return

    if len(team_start) == DEPTH:
        team1 = 0
        team2 = 0

        for k in range(1, N+1):
            if k not in team_start:
                team_link.append(k)

        for x in range(N):
            for y in range(x+1, N):
                if ((x+1) in team_start) and ((y+1) in team_start):
                    team1 += int(G[x][y]) + int(G[y][x])
                elif ((x+1) in team_link) and ((y+1) in team_link):
                    team2 += int(G[x][y]) + int(G[y][x])

        tmp = abs(team1-team2)
        min_gap[0] = min(tmp, min_gap[0])
        print(team_start, team_link)
        team_link.clear()
        team_start.pop()
        if root == N:
            team_start.pop()
        print(min_gap[0])
        return

    for j in range(root+1, N+1):
        dfs(j)


for i in range(1, N):
    dfs(i)

print(min_gap[0])
