# https://school.programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, cols, queries):
    board = [[row*cols+col+1 for col in range(cols)] for row in range(rows)]
    
    moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    answer = []
    
    for r1, c1, r2, c2 in queries:
        cnt = 0
        temp = float('inf')
        r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1
        
        crow, ccol = r1, c1
        c_point = board[crow][ccol]
        temp = min(c_point, temp)
        check = False
        while True:
            if crow == r1 and ccol == c1 and check:
                break
            check = True
            nrow, ncol = crow+moves[cnt][0], ccol+moves[cnt][1]

            if not (r1<=nrow<=r2 and c1<=ncol<=c2):
                cnt += 1
                nrow, ncol = crow+moves[cnt][0], ccol+moves[cnt][1]
                
            n_point = board[nrow][ncol]
            board[nrow][ncol] = c_point
            
            c_point = n_point
            temp = min(c_point, temp)
            crow, ccol = nrow, ncol
            
        answer.append(temp)
    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
# [8, 10, 25]
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
# [1, 1, 5, 3]
print(solution(100, 97, [[1,1,100,97]]))
# [1]

# 테스트 1 〉	통과 (0.05ms, 10.2MB)
# 테스트 2 〉	통과 (0.04ms, 10.2MB)
# 테스트 3 〉	통과 (441.07ms, 11.7MB)
# 테스트 4 〉	통과 (259.29ms, 11.2MB)
# 테스트 5 〉	통과 (340.41ms, 11.4MB)
# 테스트 6 〉	통과 (349.36ms, 11.7MB)
# 테스트 7 〉	통과 (374.76ms, 12.1MB)
# 테스트 8 〉	통과 (213.64ms, 11.2MB)
# 테스트 9 〉	통과 (297.20ms, 11.8MB)
# 테스트 10 〉	통과 (259.61ms, 11.5MB)
# 테스트 11 〉	통과 (242.67ms, 11.3MB)