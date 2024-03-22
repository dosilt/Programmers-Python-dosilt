# https://school.programmers.co.kr/learn/courses/30/lessons/172928

def find_start_pos(board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 'S':
                return [r, c]


def solution(park, routes):
    board = list(map(list, park))
    c_r, c_c = find_start_pos(board)
    
    # E = [0, 1], S = [1, 0], N = [-1, 0], W = [0, -1]
    moves = {'E': [0, 1], 'S': [1, 0], 'N': [-1, 0], 'W': [0, -1]}
    for route in routes:
        direction, cnt = route.split()
        cnt = int(cnt)
        
        dr, dc = moves[direction]
        t_r, t_c = c_r, c_c
        for _ in range(cnt):
            n_r, n_c = t_r + dr, t_c + dc
            
            if n_r < 0 or n_r >= len(board) or n_c < 0 or n_c >= len(board[0]) or board[n_r][n_c] == 'X':
                break
            t_r, t_c = n_r, n_c
        else:
            c_r, c_c = t_r, t_c
        
    return [c_r, c_c]

print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))
# [2, 1]

print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]))
# [0, 1]

print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]))
# [0, 0]


# 테스트 1 〉	통과 (0.03ms, 10.3MB)
# 테스트 2 〉	통과 (0.04ms, 10.5MB)
# 테스트 3 〉	통과 (0.09ms, 10.3MB)
# 테스트 4 〉	통과 (0.09ms, 10.4MB)
# 테스트 5 〉	통과 (0.14ms, 10.4MB)
# 테스트 6 〉	통과 (0.46ms, 10.2MB)
# 테스트 7 〉	통과 (0.38ms, 10.2MB)
# 테스트 8 〉	통과 (0.17ms, 10.5MB)
# 테스트 9 〉	통과 (0.24ms, 10.4MB)
# 테스트 10 〉	통과 (0.21ms, 10.3MB)
# 테스트 11 〉	통과 (0.38ms, 10.2MB)
# 테스트 12 〉	통과 (0.44ms, 10.4MB)
# 테스트 13 〉	통과 (0.30ms, 10.4MB)
# 테스트 14 〉	통과 (0.31ms, 10.3MB)
# 테스트 15 〉	통과 (0.24ms, 10.4MB)
# 테스트 16 〉	통과 (0.05ms, 10.4MB)
# 테스트 17 〉	통과 (0.08ms, 10.5MB)
# 테스트 18 〉	통과 (0.06ms, 10.4MB)
# 테스트 19 〉	통과 (0.19ms, 10.4MB)
# 테스트 20 〉	통과 (0.05ms, 10.5MB)