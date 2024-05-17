# https://school.programmers.co.kr/learn/courses/30/lessons/86052

def solution(grid):
    grid = list(map(list, grid))
    rows, cols = len(grid), len(grid[0])
    visited = [[False, False, False, False] for _ in range(rows*cols)]
    # 위, 오른, 아래, 왼
    moves = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    
    answer = []
    for row in range(rows):
        for col in range(cols):
            for i in range(4):
                if visited[row*cols+col][i] is False:
                    crow, ccol = row, col
                    visited[crow*cols+ccol][i] = True
                    temp = 1
                    while True:
                        nrow, ncol = (crow + moves[i][0] + rows) % rows, (ccol + moves[i][1] + cols) % cols
                        
                        if grid[nrow][ncol] == 'S':
                            i = i
                        
                        elif grid[nrow][ncol] == 'L':
                            i = (i+4-1)%4
                        
                        elif grid[nrow][ncol] == 'R':
                            i = (i+4+1)%4
                        
                        if visited[nrow*cols+ncol][i]:
                            break
                        else:
                            visited[nrow*cols+ncol][i] = True
                            crow, ccol = nrow, ncol
                        temp += 1
                            
                    answer.append(temp)
    
    return sorted(answer)

print(solution(["SL","LR"]))
[16]
print(solution(["S"]))
# [1, 1, 1, 1]
print(solution(["R","R"]))
# [4, 4]

# 테스트 1 〉	통과 (0.36ms, 10.3MB)
# 테스트 2 〉	통과 (0.42ms, 10.3MB)
# 테스트 3 〉	통과 (0.48ms, 10.2MB)
# 테스트 4 〉	통과 (23.36ms, 10.9MB)
# 테스트 5 〉	통과 (43.28ms, 11.6MB)
# 테스트 6 〉	통과 (78.88ms, 11.8MB)
# 테스트 7 〉	통과 (830.68ms, 34.1MB)
# 테스트 8 〉	통과 (554.58ms, 31.3MB)
# 테스트 9 〉	통과 (694.63ms, 35.8MB)
# 테스트 10 〉	통과 (845.11ms, 41.8MB)
# 테스트 11 〉	통과 (821.65ms, 43.6MB)