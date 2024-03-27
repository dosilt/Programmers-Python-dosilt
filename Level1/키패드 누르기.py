# https://school.programmers.co.kr/learn/courses/30/lessons/67256

from collections import deque

def move(phone, button, cur_point, max_row, max_col):
    moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    queue = deque([cur_point+[0]])
    visited = set()
    while queue:
        cr, cc, dis = queue.popleft()
        visited.add((cr, cc))
        if phone[cr][cc] == button:
            return cr, cc, dis
        
        for dr, dc in moves:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < max_row and 0 <= nc < max_col and (nr, nc) not in visited:
                queue.append([cr+dr, cc+dc, dis+1])

def select_hand(phone, button, cur_left, cur_right, max_row, max_col, prefer):
    lr, lc, left_cnt = move(phone, button, cur_left, max_row, max_col)
    rr, rc, right_cnt = move(phone, button, cur_right, max_row, max_col)
    
    if left_cnt == right_cnt:
        if prefer == 'right':
            cur_right = [rr, rc]
            return cur_left, cur_right, 'R'
        else:
            cur_left = [lr, rc]
            return cur_left, cur_right, 'L'
    
    elif left_cnt < right_cnt:
        cur_left = [lr, lc]
        return cur_left, cur_right, 'L'
    
    else:
        cur_right = [rr, rc]
        return cur_left, cur_right, 'R'

def rule_base(number, cur_left, cur_right):
    result = ''
    if number == 1:
        cur_left = [0, 0]
        result = 'L'
    elif number == 4:
        cur_left = [1, 0]
        result = 'L'
    elif number == 7:
        cur_left = [2, 0]
        result = 'L'
        
    elif number == 3:
        cur_right = [0, 2]
        result = 'R'
    elif number == 6:
        cur_right = [1, 2]
        result = 'R'
    elif number == 9:
        cur_right = [2, 2]
        result = 'R'
        
    return cur_left, cur_right, result
        
def solution(numbers, hand):
    phone = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]
    left_start, right_start = [3, 0], [3, 2]
    max_row, max_col = 4, 3
    
    answer = ''
    for number in numbers:
        if number in [1, 4, 7, 3, 6, 9]:
            left_start, right_start, result = rule_base(number,  left_start, right_start)
        else:
            left_start, right_start, result = select_hand(phone, number, left_start, right_start, max_row, max_col, hand)
        answer += result
        
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
# "LRLLLRLLRRL"
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
# "LRLLRRLLLRR"
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
# "LLRLLRLLRL"

# 테스트 1 〉	통과 (0.00ms, 10.4MB)
# 테스트 2 〉	통과 (0.08ms, 10.4MB)
# 테스트 3 〉	통과 (0.05ms, 10.3MB)
# 테스트 4 〉	통과 (0.00ms, 10.3MB)
# 테스트 5 〉	통과 (0.02ms, 10.3MB)
# 테스트 6 〉	통과 (0.02ms, 10.3MB)
# 테스트 7 〉	통과 (0.11ms, 10.4MB)
# 테스트 8 〉	통과 (0.15ms, 10.3MB)
# 테스트 9 〉	통과 (0.10ms, 10.3MB)
# 테스트 10 〉	통과 (0.09ms, 10.4MB)
# 테스트 11 〉	통과 (0.43ms, 10.4MB)
# 테스트 12 〉	통과 (0.34ms, 10.3MB)
# 테스트 13 〉	통과 (0.67ms, 10.3MB)
# 테스트 14 〉	통과 (1.17ms, 10.3MB)
# 테스트 15 〉	통과 (2.99ms, 10.3MB)
# 테스트 16 〉	통과 (3.34ms, 10.3MB)
# 테스트 17 〉	통과 (8.01ms, 10.3MB)
# 테스트 18 〉	통과 (6.20ms, 10.3MB)
# 테스트 19 〉	통과 (6.27ms, 10.3MB)
# 테스트 20 〉	통과 (5.60ms, 10.4MB)