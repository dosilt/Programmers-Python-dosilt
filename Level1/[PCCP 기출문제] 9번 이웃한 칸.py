# https://school.programmers.co.kr/learn/courses/30/lessons/250125

def solution(board, h, w):
    moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    size = len(board)
    color = board[h][w]
    answer = 0
    for dr, dc in moves:
        if 0 <= h+dr < size and 0 <= w+dc < size and color == board[h+dr][w+dc]:
            answer += 1
    return answer

print(solution([["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]], 1, 1))
# 2
print(solution([["yellow", "green", "blue"], ["blue", "green", "yellow"], ["yellow", "blue", "blue"]], 0, 1))
# 1

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.00ms, 10.1MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.1MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 9.99MB)
# 테스트 7 〉	통과 (0.00ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 9.99MB)
# 테스트 9 〉	통과 (0.01ms, 10.2MB)
# 테스트 10 〉	통과 (0.01ms, 10.3MB)
# 테스트 11 〉	통과 (0.00ms, 10.1MB)
# 테스트 12 〉	통과 (0.01ms, 10.3MB)
# 테스트 13 〉	통과 (0.01ms, 10.1MB)
# 테스트 14 〉	통과 (0.01ms, 10.1MB)
# 테스트 15 〉	통과 (0.00ms, 10.1MB)
# 테스트 16 〉	통과 (0.01ms, 10.3MB)
# 테스트 17 〉	통과 (0.01ms, 10.1MB)
# 테스트 18 〉	통과 (0.00ms, 10.2MB)
# 테스트 19 〉	통과 (0.00ms, 10.1MB)
# 테스트 20 〉	통과 (0.01ms, 10.3MB)
# 테스트 21 〉	통과 (0.01ms, 10.1MB)
# 테스트 22 〉	통과 (0.01ms, 10MB)
# 테스트 23 〉	통과 (0.01ms, 10.3MB)
# 테스트 24 〉	통과 (0.01ms, 10.2MB)
# 테스트 25 〉	통과 (0.01ms, 10.1MB)
# 테스트 26 〉	통과 (0.01ms, 10.2MB)
# 테스트 27 〉	통과 (0.01ms, 10.1MB)
# 테스트 28 〉	통과 (0.01ms, 10.3MB)
# 테스트 29 〉	통과 (0.01ms, 10.1MB)
# 테스트 30 〉	통과 (0.00ms, 10.1MB)
# 테스트 31 〉	통과 (0.00ms, 10.2MB)
# 테스트 32 〉	통과 (0.00ms, 10.2MB)
# 테스트 33 〉	통과 (0.00ms, 10.2MB)
# 테스트 34 〉	통과 (0.00ms, 10.2MB)
# 테스트 35 〉	통과 (0.00ms, 10.1MB)
# 테스트 36 〉	통과 (0.00ms, 10.2MB)
# 테스트 37 〉	통과 (0.01ms, 10.2MB)
# 테스트 38 〉	통과 (0.00ms, 10.1MB)
# 테스트 39 〉	통과 (0.00ms, 9.97MB)
# 테스트 40 〉	통과 (0.00ms, 10.2MB)
# 테스트 41 〉	통과 (0.00ms, 10.1MB)
# 테스트 42 〉	통과 (0.00ms, 10MB)
# 테스트 43 〉	통과 (0.00ms, 10.2MB)
# 테스트 44 〉	통과 (0.01ms, 10.2MB)
# 테스트 45 〉	통과 (0.00ms, 10MB)
# 테스트 46 〉	통과 (0.01ms, 10.1MB)
# 테스트 47 〉	통과 (0.01ms, 10.3MB)
# 테스트 48 〉	통과 (0.00ms, 10.1MB)
# 테스트 49 〉	통과 (0.01ms, 10.1MB)
# 테스트 50 〉	통과 (0.00ms, 10.2MB)