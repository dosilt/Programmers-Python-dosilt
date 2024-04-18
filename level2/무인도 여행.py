# https://school.programmers.co.kr/learn/courses/30/lessons/154540

from collections import deque

def bfs(row, col, rows, cols, maps, result):
    moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    queue = deque([[row, col]])
    while queue:
        cr, cc = queue.popleft()
        
        for dr, dc in moves:
            nr, nc = cr+dr, cc+dc
            if 0<=nr<rows and 0<=nc<cols and maps[nr][nc] != 'X':
                result += int(maps[nr][nc])
                maps[nr][nc] = 'X'
                queue.append([nr, nc])
    return result, maps

def solution(maps):
    maps = list(map(list, maps))
    rows, cols = len(maps), len(maps[0])
    answer = []
    
    for row in range(rows):
        for col in range(cols):
            if maps[row][col] != 'X':
                result = int(maps[row][col])
                maps[row][col] = 'X'
                result, maps = bfs(row, col, rows, cols, maps, result)
                answer.append(result)
    
    if answer == []:
        return [-1]
    return sorted(answer)

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))
# [1, 1, 27]
print(solution(["XXX","XXX","XXX"]))
# [-1]

# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.04ms, 10.5MB)
# 테스트 3 〉	통과 (0.06ms, 10.4MB)
# 테스트 4 〉	통과 (0.12ms, 10.2MB)
# 테스트 5 〉	통과 (0.96ms, 10.3MB)
# 테스트 6 〉	통과 (1.30ms, 10.3MB)
# 테스트 7 〉	통과 (1.30ms, 10.4MB)
# 테스트 8 〉	통과 (2.80ms, 10.6MB)
# 테스트 9 〉	통과 (5.97ms, 10.4MB)
# 테스트 10 〉	통과 (6.07ms, 10.4MB)
# 테스트 11 〉	통과 (3.21ms, 10.5MB)
# 테스트 12 〉	통과 (7.63ms, 10.5MB)
# 테스트 13 〉	통과 (8.23ms, 10.5MB)
# 테스트 14 〉	통과 (6.95ms, 10.4MB)
# 테스트 15 〉	통과 (7.43ms, 10.4MB)
# 테스트 16 〉	통과 (9.11ms, 10.5MB)
# 테스트 17 〉	통과 (0.52ms, 10.3MB)
# 테스트 18 〉	통과 (8.82ms, 10.5MB)
# 테스트 19 〉	통과 (8.96ms, 10.4MB)
# 테스트 20 〉	통과 (0.74ms, 10.3MB)
# 테스트 21 〉	통과 (0.70ms, 10.3MB)
# 테스트 22 〉	통과 (0.08ms, 10.4MB)
# 테스트 23 〉	통과 (8.65ms, 10.7MB)
# 테스트 24 〉	통과 (10.27ms, 10.4MB)
# 테스트 25 〉	통과 (0.24ms, 10.4MB)