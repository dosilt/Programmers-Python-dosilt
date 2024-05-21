# https://school.programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    moves = [[1, 0], [0, 1], [-1, -1]]
    board[0][0] = 1
    
    row, col, cnt = 0, 0, 1
    for s, i in enumerate(range(n, -1, -1)):
        dr, dc = moves[s%3]
        
        while True:
            if 0<=row+dr<n and 0<=col+dc<n and board[row+dr][col+dc] == 0:
                row, col = row + dr, col+dc
                cnt += 1
                board[row][col] = cnt
            else:
                break
    
    
    answer= []
    for n, b in enumerate(board):
        answer.extend(b[:n+1])
    
    return answer


print(solution(4))
# [1,2,9,3,10,8,4,5,6,7]
print(solution(5))
# [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
print(solution(6))
# [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]

# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.4MB)
# 테스트 3 〉	통과 (0.02ms, 10.1MB)
# 테스트 4 〉	통과 (2.59ms, 10.6MB)
# 테스트 5 〉	통과 (1.89ms, 10.6MB)
# 테스트 6 〉	통과 (1.82ms, 10.5MB)
# 테스트 7 〉	통과 (212.37ms, 42.9MB)
# 테스트 8 〉	통과 (211.39ms, 42.7MB)
# 테스트 9 〉	통과 (225.38ms, 42.8MB)