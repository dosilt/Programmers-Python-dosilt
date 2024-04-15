# https://school.programmers.co.kr/learn/courses/30/lessons/169199

from collections import deque

def pos(rows, cols, board):
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == '.' or board[row][col] == 'D':
                continue
            elif board[row][col] == 'R':
                robot = [row, col]
                board[row][col] = '.'
            elif board[row][col] == 'G':
                goal = [row, col]
                board[row][col] = '.'
    return board, robot, goal

def moving(crow, ccol, dr, dc, rows, cols, board):
    while True:
        nrow, ncol = crow + dr, ccol + dc
        if 0 <= nrow < rows and 0 <= ncol < cols and board[nrow][ncol] == '.':
            crow, ccol = nrow, ncol
        else:
            return crow, ccol
    


def bfs(rows, cols, goal, robot, board, visited):
    robots = deque([robot+[0]])
    moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    
    while robots:
        crow, ccol, cnt = robots.popleft()
        
        for dr, dc in moves:
            nrow, ncol = moving(crow, ccol, dr, dc, rows, cols, board)
            if goal == [nrow, ncol]:
                return cnt+1
            if visited[nrow][ncol]:
                continue
            
            robots.append([nrow, ncol, cnt+1])
            visited[nrow][ncol] = True
    return -1

def solution(board):
    board = list(map(list, board))
    rows, cols = len(board), len(board[0])
    board, robot, goal = pos(rows, cols, board)
    
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[robot[0]][robot[1]] = True
    
    answer = bfs(rows, cols, goal, robot, board, visited)
    return answer


print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
# 7
print(solution([".D.R", "....", ".G..", "...D"]))
# -1 

# 테스트 1 〉	통과 (4.59ms, 10.3MB)
# 테스트 2 〉	통과 (3.85ms, 10.6MB)
# 테스트 3 〉	통과 (0.47ms, 10.4MB)
# 테스트 4 〉	통과 (2.37ms, 10.3MB)
# 테스트 5 〉	통과 (1.47ms, 10.5MB)
# 테스트 6 〉	통과 (0.54ms, 10.3MB)
# 테스트 7 〉	통과 (5.91ms, 10.4MB)
# 테스트 8 〉	통과 (0.70ms, 10.3MB)
# 테스트 9 〉	통과 (2.00ms, 10.3MB)
# 테스트 10 〉	통과 (3.51ms, 10.3MB)
# 테스트 11 〉	통과 (0.07ms, 10.4MB)
# 테스트 12 〉	통과 (0.05ms, 10.3MB)
# 테스트 13 〉	통과 (0.19ms, 10.5MB)
# 테스트 14 〉	통과 (0.51ms, 10.3MB)
# 테스트 15 〉	통과 (0.28ms, 10.4MB)
# 테스트 16 〉	통과 (2.23ms, 10.3MB)
# 테스트 17 〉	통과 (0.48ms, 10.3MB)
# 테스트 18 〉	통과 (0.89ms, 10.4MB)
# 테스트 19 〉	통과 (2.01ms, 10.3MB)
# 테스트 20 〉	통과 (0.13ms, 10.3MB)
# 테스트 21 〉	통과 (5.99ms, 10.4MB)
# 테스트 22 〉	통과 (0.88ms, 10.4MB)
# 테스트 23 〉	통과 (0.30ms, 10.4MB)
# 테스트 24 〉	통과 (6.07ms, 10.3MB)
# 테스트 25 〉	통과 (2.32ms, 10.4MB)
# 테스트 26 〉	통과 (2.21ms, 10.3MB)
# 테스트 27 〉	통과 (0.66ms, 10.3MB)