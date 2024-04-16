# https://school.programmers.co.kr/learn/courses/30/lessons/169198

def up(m, n, cx, cy, bx, by):
    return (cx - bx)**2 + ((m-cy) + (m-by))**2

def down(m, n, cx, cy, bx, by):
    return (cx - bx)**2 + (cy + by)**2

def left(m, n, cx, cy, bx, by):
    return (cx + bx)**2 + (cy-by)**2

def right(m, n, cx, cy, bx, by):
    return (n-cx + n-bx)**2 + (cy-by)**2


def solution(n, m, startX, startY, balls):
    answer = []
    for bx, by in balls:
        a = [float('inf')] * 4
        if startY > by or startX != bx:
            a[0] = up(m, n, startX, startY, bx, by)
        if startY < by or startX != bx:
            a[1] = down(m, n, startX, startY, bx, by)
        if startX < bx or startY != by:
            a[2] = left(m, n, startX, startY, bx, by)
        if startX > bx or startY != by:
            a[3] = right(m, n, startX, startY, bx, by)
            
        answer.append(min(a))
    return answer

print(solution(10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]]))
# [52, 37, 116]


# 테스트 1 〉	통과 (2.33ms, 10.3MB)
# 테스트 2 〉	통과 (4.92ms, 10.3MB)
# 테스트 3 〉	통과 (0.29ms, 10.4MB)
# 테스트 4 〉	통과 (1.39ms, 10.3MB)
# 테스트 5 〉	통과 (0.30ms, 10.3MB)
# 테스트 6 〉	통과 (3.81ms, 10.3MB)
# 테스트 7 〉	통과 (3.67ms, 10.6MB)
# 테스트 8 〉	통과 (0.54ms, 10.3MB)
# 테스트 9 〉	통과 (1.24ms, 10.4MB)
# 테스트 10 〉	통과 (2.30ms, 10.4MB)
# 테스트 11 〉	통과 (2.56ms, 10.3MB)
# 테스트 12 〉	통과 (4.16ms, 10.3MB)
# 테스트 13 〉	통과 (5.11ms, 10.3MB)
# 테스트 14 〉	통과 (0.24ms, 10.2MB)
# 테스트 15 〉	통과 (1.42ms, 10.2MB)
# 테스트 16 〉	통과 (1.24ms, 10.3MB)
# 테스트 17 〉	통과 (0.88ms, 10.3MB)
# 테스트 18 〉	통과 (2.33ms, 10.2MB)
# 테스트 19 〉	통과 (2.20ms, 10.2MB)
# 테스트 20 〉	통과 (2.93ms, 10.5MB)
# 테스트 21 〉	통과 (2.36ms, 10.3MB)
# 테스트 22 〉	통과 (1.60ms, 10.4MB)
# 테스트 23 〉	통과 (0.63ms, 10.3MB)
# 테스트 24 〉	통과 (1.72ms, 10.2MB)
# 테스트 25 〉	통과 (1.68ms, 10.3MB)
# 테스트 26 〉	통과 (1.14ms, 10.1MB)
# 테스트 27 〉	통과 (0.32ms, 10.4MB)
# 테스트 28 〉	통과 (2.13ms, 10.1MB)
# 테스트 29 〉	통과 (0.01ms, 10.3MB)
# 테스트 30 〉	통과 (0.01ms, 10.2MB)
# 테스트 31 〉	통과 (3.47ms, 10.3MB)
# 테스트 32 〉	통과 (2.27ms, 10.3MB)
# 테스트 33 〉	통과 (0.23ms, 10.3MB)
# 테스트 34 〉	통과 (1.30ms, 10.4MB)
# 테스트 35 〉	통과 (0.43ms, 10.2MB)
# 테스트 36 〉	통과 (1.71ms, 10.3MB)