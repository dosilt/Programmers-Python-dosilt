# https://school.programmers.co.kr/learn/courses/30/lessons/64061

from collections import deque

def column_check(board, col):
    for row in range(len(board)):
        if board[row][col] != 0:
            return row, col
    else:
        return -1, -1


def solution(board, moves):
    queue = deque([0])
    answer = 0
    for move in moves:
        row, col = column_check(board, move-1)
        if row != -1 and col != -1:
            doll = board[row][col]
            board[row][col] = 0
            if queue[-1] == doll:
                queue.pop()
                answer += 2
            else:
                queue.append(doll)

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
# 4


# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.03ms, 10MB)
# 테스트 3 〉	통과 (0.02ms, 10.1MB)
# 테스트 4 〉	통과 (1.27ms, 10.3MB)
# 테스트 5 〉	통과 (0.02ms, 10.3MB)
# 테스트 6 〉	통과 (0.04ms, 10.2MB)
# 테스트 7 〉	통과 (0.08ms, 9.96MB)
# 테스트 8 〉	통과 (0.30ms, 10.2MB)
# 테스트 9 〉	통과 (0.28ms, 10MB)
# 테스트 10 〉	통과 (0.32ms, 10.2MB)
# 테스트 11 〉	통과 (0.70ms, 10.2MB)