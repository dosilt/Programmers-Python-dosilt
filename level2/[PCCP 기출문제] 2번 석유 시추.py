# https://school.programmers.co.kr/learn/courses/30/lessons/250136

from collections import deque

def bfs(cur_point, rows, cols, land):
    moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    cur_point = deque([cur_point])
    temp, cnt = [], 0
    while cur_point:
        cr, cc = cur_point.popleft()
        cnt += 1
        
        for i, (dr, dc) in enumerate(moves):
            nr, nc = cr+dr, cc+dc
            
            if 0 <= nr < rows and 0 <= nc < cols and land[nr][nc] == 1:
                land[nr][nc] = 0
                cur_point.append([nr, nc])
            else:
                if i == 0:
                    temp.append([cr, cc])
                    
    temp = sorted(temp, key=lambda x:[x[1], -x[0]])
    return temp, cnt
    
def solution(land):
    rows, cols = len(land), len(land[0])
    
    scores = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for row in range(rows):
        for col in range(cols):
            if land[row][col] == 1:
                land[row][col] = 0
                temp, cnt = bfs([row, col], rows, cols, land)
                cur_c = -1
                for r, c in temp:
                    if cur_c != c:
                        scores[r][c] = cnt
                        cur_c = c
                        
    answer = 0
    for col in range(cols):
        temp = 0
        for row in range(rows):
            temp += scores[row][col]
        answer = max(answer, temp)
    return answer



print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))
# 9
print(solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]))
# 16

# 정확성  테스트
# 테스트 1 〉	통과 (0.06ms, 10.4MB)
# 테스트 2 〉	통과 (0.31ms, 10.4MB)
# 테스트 3 〉	통과 (0.10ms, 10.3MB)
# 테스트 4 〉	통과 (0.15ms, 10.3MB)
# 테스트 5 〉	통과 (0.11ms, 10.2MB)
# 테스트 6 〉	통과 (0.94ms, 10.2MB)
# 테스트 7 〉	통과 (1.47ms, 10.4MB)
# 테스트 8 〉	통과 (0.64ms, 10.2MB)
# 테스트 9 〉	통과 (4.26ms, 10.5MB)
# 효율성  테스트
# 테스트 1 〉	통과 (88.76ms, 17.4MB)
# 테스트 2 〉	통과 (177.76ms, 14.3MB)
# 테스트 3 〉	통과 (192.10ms, 14.3MB)
# 테스트 4 〉	통과 (74.86ms, 16.9MB)
# 테스트 5 〉	통과 (549.29ms, 63.1MB)
# 테스트 6 〉	통과 (81.72ms, 18MB)