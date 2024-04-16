# https://school.programmers.co.kr/learn/courses/30/lessons/159993

from collections import deque

def pos(rows, cols, maps):
    for row in range(rows):
        for col in range(cols):
            if maps[row][col] == 'S':
                start = [row, col]
            elif maps[row][col] == 'L':
                lever = [row, col]
            elif maps[row][col] == 'E':
                exit = [row, col]
    return start, lever, exit

def bfs(cr, cc, gr, gc, rows, cols, maps, visited):
    moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    queue = deque([[cr, cc, 0]])
    
    while queue:
        r, c, cnt = queue.popleft()
        
        if gr == r and gc == c:
            return cnt
        
        for dr, dc in moves:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and maps[nr][nc] != 'X' and visited[nr][nc] is False:
                visited[nr][nc] = True
                queue.append([nr, nc, cnt+1])

    return -1

def solution(maps):
    maps = list(map(list, maps))
    rows, cols = len(maps), len(maps[0])
    
    start, lever, exit = pos(rows, cols, maps)
    
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    s2l = bfs(start[0], start[1], lever[0], lever[1], rows, cols, maps, visited)
    if s2l == -1:
        return -1
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    l2g = bfs(lever[0], lever[1], exit[0], exit[1], rows, cols, maps, visited)
    if l2g == -1:
        return -1
    return s2l + l2g

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
# 16
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))
# -1

# 테스트 1 〉	통과 (0.05ms, 10.3MB)
# 테스트 2 〉	통과 (0.12ms, 10.3MB)
# 테스트 3 〉	통과 (0.27ms, 10.2MB)
# 테스트 4 〉	통과 (0.12ms, 10.2MB)
# 테스트 5 〉	통과 (0.16ms, 10.2MB)
# 테스트 6 〉	통과 (0.10ms, 10.2MB)
# 테스트 7 〉	통과 (1.73ms, 10.3MB)
# 테스트 8 〉	통과 (3.88ms, 10.2MB)
# 테스트 9 〉	통과 (0.04ms, 10.4MB)
# 테스트 10 〉	통과 (0.03ms, 10.4MB)
# 테스트 11 〉	통과 (0.71ms, 10.2MB)
# 테스트 12 〉	통과 (4.25ms, 10.4MB)
# 테스트 13 〉	통과 (5.15ms, 10.2MB)
# 테스트 14 〉	통과 (3.87ms, 10.2MB)
# 테스트 15 〉	통과 (0.70ms, 10.5MB)
# 테스트 16 〉	통과 (9.14ms, 10.6MB)
# 테스트 17 〉	통과 (12.22ms, 10.4MB)
# 테스트 18 〉	통과 (0.24ms, 10.2MB)
# 테스트 19 〉	통과 (0.18ms, 10.2MB)
# 테스트 20 〉	통과 (8.23ms, 10.4MB)
# 테스트 21 〉	통과 (1.73ms, 10.2MB)
# 테스트 22 〉	통과 (0.19ms, 10.3MB)
# 테스트 23 〉	통과 (0.05ms, 10.2MB)