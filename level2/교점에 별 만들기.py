# https://school.programmers.co.kr/learn/courses/30/lessons/87377

def cross_point(line1, line2):
    a, b, e = line1
    c, d, f = line2
    
    temp = a*d - b*c
    if temp == 0:
        return float('inf'), float('inf')
    
    x_head = (b*f - e*d) / temp
    y_head = (e*c - a*f) / temp
    
    if x_head == int(x_head) and y_head == int(y_head):
        return int(x_head), int(y_head)
    return float('inf'), float('inf')

def solution(lines):
    cross_x, cross_y = [], []
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            x, y = cross_point(lines[i], lines[j])
            if x != float('inf'):
                cross_x.append(x)
                cross_y.append(y)
            
    min_x, max_x = min(cross_x), max(cross_x)
    min_y, max_y = min(cross_y), max(cross_y)
    
    board = [['.' for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
    
    for x, y in zip(cross_x, cross_y):
        x -= min_x
        y -= min_y
        board[y][x] = '*'
    
    answer = []
    for b in board:
        answer.append(''.join(b))
    return answer[::-1]

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
# ["....*....", ".........", ".........", "*.......*", ".........", ".........", ".........", ".........", "*.......*"]
# print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
# # ["*.*"]
# print(solution([[1, -1, 0], [2, -1, 0]]))
# # ["*"]
# print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))
# # ["*"]

# 테스트 1 〉	통과 (0.25ms, 10.2MB)
# 테스트 2 〉	통과 (9.06ms, 12.3MB)
# 테스트 3 〉	통과 (0.13ms, 10.3MB)
# 테스트 4 〉	통과 (20.72ms, 14.9MB)
# 테스트 5 〉	통과 (4.98ms, 11.5MB)
# 테스트 6 〉	통과 (1.51ms, 10.4MB)
# 테스트 7 〉	통과 (8.08ms, 12MB)
# 테스트 8 〉	통과 (0.09ms, 10.1MB)
# 테스트 9 〉	통과 (307.59ms, 10.6MB)
# 테스트 10 〉	통과 (315.52ms, 10.4MB)
# 테스트 11 〉	통과 (393.75ms, 10.3MB)
# 테스트 12 〉	통과 (442.56ms, 10.5MB)
# 테스트 13 〉	통과 (485.28ms, 11.1MB)
# 테스트 14 〉	통과 (419.27ms, 11.2MB)
# 테스트 15 〉	통과 (388.01ms, 10.4MB)
# 테스트 16 〉	통과 (341.63ms, 10.3MB)
# 테스트 17 〉	통과 (389.58ms, 11.4MB)
# 테스트 18 〉	통과 (402.49ms, 11MB)
# 테스트 19 〉	통과 (386.21ms, 10.4MB)
# 테스트 20 〉	통과 (297.30ms, 10.3MB)
# 테스트 21 〉	통과 (324.12ms, 12.1MB)
# 테스트 22 〉	통과 (0.12ms, 10.3MB)
# 테스트 23 〉	통과 (0.06ms, 10.2MB)
# 테스트 24 〉	통과 (0.03ms, 10.2MB)
# 테스트 25 〉	통과 (0.09ms, 10.4MB)
# 테스트 26 〉	통과 (0.25ms, 10.2MB)
# 테스트 27 〉	통과 (0.01ms, 10.2MB)
# 테스트 28 〉	통과 (0.02ms, 10.3MB)
# 테스트 29 〉	통과 (0.01ms, 10.3MB)

