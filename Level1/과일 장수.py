# https://school.programmers.co.kr/learn/courses/30/lessons/135808

import heapq

def solution(k, m, score):
    heapq._heapify_max(score)
    
    answer, cnt = 0, 0
    while score:
        cur_value = heapq._heappop_max(score)
        cnt += 1
        if cnt == m:
            answer += cur_value * m
            cnt = 0
    
    return answer

print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
# 8
print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))
# 33


# 테스트 1 〉	통과 (0.04ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.03ms, 10.4MB)
# 테스트 4 〉	통과 (0.01ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (26.14ms, 10.6MB)
# 테스트 7 〉	통과 (31.27ms, 10.7MB)
# 테스트 8 〉	통과 (3.99ms, 10.4MB)
# 테스트 9 〉	통과 (29.50ms, 10.6MB)
# 테스트 10 〉	통과 (20.82ms, 10.5MB)
# 테스트 11 〉	통과 (455.12ms, 18.6MB)
# 테스트 12 〉	통과 (501.74ms, 18.6MB)
# 테스트 13 〉	통과 (431.96ms, 18.6MB)
# 테스트 14 〉	통과 (431.59ms, 18.5MB)
# 테스트 15 〉	통과 (429.80ms, 18.5MB)
# 테스트 16 〉	통과 (0.01ms, 10.2MB)
# 테스트 17 〉	통과 (0.00ms, 10.1MB)
# 테스트 18 〉	통과 (0.03ms, 10.2MB)
# 테스트 19 〉	통과 (0.02ms, 10.3MB)
# 테스트 20 〉	통과 (0.02ms, 10.4MB)
# 테스트 21 〉	통과 (0.01ms, 10.2MB)
# 테스트 22 〉	통과 (0.01ms, 10.4MB)
# 테스트 23 〉	통과 (0.01ms, 10.2MB)
# 테스트 24 〉	통과 (0.01ms, 10.2MB)