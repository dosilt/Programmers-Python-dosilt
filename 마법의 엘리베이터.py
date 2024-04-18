# https://school.programmers.co.kr/learn/courses/30/lessons/148653

from collections import deque

def bfs(num):
    queue = deque([[num, 0]])
    answer = []
    while queue:
        n, cnt = queue.popleft()
        a, b = divmod(n, 10)
        if a == 0:
            answer.append(min(cnt + b, cnt + 10 - b + 1))
            continue
        
        if b < 5:
            queue.append([a, b+cnt])
        elif b == 5:
            queue.append([a, b+cnt])
            queue.append([a+1, 10-b+cnt])
        elif b > 5:
            queue.append([a+1, 10-b+cnt])
    return min(answer)        

def solution(storey):
    return bfs(storey)

print(solution(16))
# 6
print(solution(2554))
# 16
print(solution(95))

# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.01ms, 10.2MB)
# 테스트 8 〉	통과 (0.02ms, 10.2MB)
# 테스트 9 〉	통과 (0.02ms, 10.3MB)
# 테스트 10 〉	통과 (0.01ms, 10.2MB)
# 테스트 11 〉	통과 (0.02ms, 10.2MB)
# 테스트 12 〉	통과 (0.01ms, 10.2MB)
# 테스트 13 〉	통과 (0.01ms, 10.2MB)