# https://school.programmers.co.kr/learn/courses/30/lessons/160585

def count_error(rows, cols, board):
    o_turn = 0
    x_turn = 0
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 'O':
                o_turn += 1
            elif board[row][col] == 'X':
                x_turn += 1
    return o_turn, x_turn
    
def done_check(board):
    cases = [[[0, 0], [0, 1], [0, 2]],
            [[0, 0], [1, 0], [2, 0]],
            [[0, 0], [1, 1], [2, 2]],
            [[0, 2], [1, 2], [2, 2]],
            [[2, 0], [2, 1], [2, 2]],
            [[2, 0], [1, 1], [0, 2]],
            [[0, 1], [1, 1], [2, 1]],
            [[1, 0], [1, 1], [1, 2]]]
    
    dictionary = {'O': False, 'X': False}
    for case in cases:
        temp = board[case[0][0]][case[0][1]]
        for r, c in case[1:]:
            if board[r][c] == temp:
                continue
            else:
                break
        else:
            dictionary[temp] = True
    return dictionary
    
def solution(board):
    for b in board:
        print(b)
    board = list(map(list, board))
    rows, cols = len(board), len(board[0])
    
    o_turn, x_turn = count_error(rows, cols, board)
    
    if o_turn == 0 and x_turn == 0:
        return 1
    elif x_turn > o_turn:
        return 0
    else:
        dictionary = done_check(board)
        if dictionary['O'] and dictionary['X']:
            return 0
        
        elif dictionary['O']:
            if o_turn == x_turn+1:
                return 1
            return 0
        
        elif dictionary['X']:
            if x_turn == o_turn:
                return 1
            return 0
        
        elif x_turn <= o_turn <= x_turn+1:
            return 1
        return 0
            
print(solution(["O.X", ".O.", "..X"]))
# 1
print(solution(["OOO", "...", "XXX"]))
# 0
print(solution(["...", ".X.", "..."]))
# 0
print(solution(["...", "...", "..."]))
# 1

# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.02ms, 10.2MB)
# 테스트 4 〉	통과 (0.02ms, 10.1MB)
# 테스트 5 〉	통과 (0.01ms, 10.3MB)
# 테스트 6 〉	통과 (0.02ms, 10.4MB)
# 테스트 7 〉	통과 (0.02ms, 10.3MB)
# 테스트 8 〉	통과 (0.02ms, 10.3MB)
# 테스트 9 〉	통과 (0.02ms, 10.3MB)
# 테스트 10 〉	통과 (0.02ms, 10.2MB)
# 테스트 11 〉	통과 (0.02ms, 10.1MB)
# 테스트 12 〉	통과 (0.02ms, 10.2MB)
# 테스트 13 〉	통과 (0.02ms, 10.2MB)
# 테스트 14 〉	통과 (0.02ms, 10.2MB)
# 테스트 15 〉	통과 (0.02ms, 10.3MB)
# 테스트 16 〉	통과 (0.01ms, 10.3MB)
# 테스트 17 〉	통과 (0.02ms, 10.3MB)
# 테스트 18 〉	통과 (0.01ms, 10.2MB)
# 테스트 19 〉	통과 (0.02ms, 10.1MB)
# 테스트 20 〉	통과 (0.02ms, 10.1MB)
# 테스트 21 〉	통과 (0.02ms, 10.3MB)
# 테스트 22 〉	통과 (0.02ms, 10.2MB)
# 테스트 23 〉	통과 (0.02ms, 10.3MB)
# 테스트 24 〉	통과 (0.02ms, 10.1MB)
# 테스트 25 〉	통과 (0.02ms, 10.3MB)
# 테스트 26 〉	통과 (0.02ms, 10.2MB)
# 테스트 27 〉	통과 (0.01ms, 10.2MB)
# 테스트 28 〉	통과 (0.02ms, 10.1MB)
# 테스트 29 〉	통과 (0.02ms, 10.3MB)
# 테스트 30 〉	통과 (0.05ms, 10.2MB)
# 테스트 31 〉	통과 (0.03ms, 10.3MB)
# 테스트 32 〉	통과 (0.02ms, 10.3MB)
# 테스트 33 〉	통과 (0.02ms, 10.1MB)
# 테스트 34 〉	통과 (0.02ms, 10.5MB)
# 테스트 35 〉	통과 (0.03ms, 10.2MB)
# 테스트 36 〉	통과 (0.02ms, 10.2MB)
# 테스트 37 〉	통과 (0.02ms, 10.3MB)
# 테스트 38 〉	통과 (0.03ms, 10.2MB)
# 테스트 39 〉	통과 (0.02ms, 10.3MB)
# 테스트 40 〉	통과 (0.02ms, 10.4MB)
# 테스트 41 〉	통과 (0.02ms, 10.3MB)
# 테스트 42 〉	통과 (0.02ms, 10.1MB)
# 테스트 43 〉	통과 (0.02ms, 10.3MB)
# 테스트 44 〉	통과 (0.03ms, 10.2MB)
# 테스트 45 〉	통과 (0.02ms, 10.2MB)
# 테스트 46 〉	통과 (0.02ms, 10.3MB)
# 테스트 47 〉	통과 (0.02ms, 10.3MB)
# 테스트 48 〉	통과 (0.02ms, 10.4MB)
# 테스트 49 〉	통과 (0.02ms, 10.2MB)
# 테스트 50 〉	통과 (0.02ms, 10.3MB)
# 테스트 51 〉	통과 (0.01ms, 10.4MB)
# 테스트 52 〉	통과 (0.02ms, 10.2MB)
# 테스트 53 〉	통과 (0.02ms, 10.3MB)
# 테스트 54 〉	통과 (0.02ms, 10.4MB)