import sys
from collections import deque

def Chess(start_x, start_y ,goal_x, goal_y):
    dx = [1,2,1,2,-1,-2,-1,-2]
    dy = [2,1,-2,-1,2,1,-2,-1]
    queue = deque([[start_x, start_y]])

    while queue:
        target = queue.popleft()
        target_x, target_y = target
        cnt = chessboard[target_x][target_y]

        if start_x == goal_x and start_y==goal_y:
            print(cnt)
            return
        else:
            for i in range(8):
                x = target_x + dx[i]
                y = target_y+ dy[i]

                if 0<=x<I and 0<=y<I and chessboard[x][y] == 0:
                    if x == goal_x and y== goal_y:
                        print(cnt+1)
                        return
                    else:
                        chessboard[x][y] = cnt + 1
                        queue.append([x,y])

N = int(sys.stdin.readline())

for _ in range(N):
    I = int(sys.stdin.readline())
    chessboard = [[0]*I for _ in range(I)]
    start_x, start_y = map(int, sys.stdin.readline().split())
    goal_x, goal_y= map(int, sys.stdin.readline().split())
    Chess(start_x, start_y ,goal_x, goal_y)

#통과(bfs)