# https://school.programmers.co.kr/learn/courses/30/lessons/142085

import heapq

def solution(n, k, enemy):
    queue = enemy[:k]
    if len(enemy) <= k:
        return len(enemy)
    
    heapq.heapify(queue)
    for i in range(k, len(enemy)):
        if queue[0] < enemy[i]:
            temp = heapq.heappop(queue)
            n -= temp
            heapq.heappush(queue, enemy[i])
            
        else:
            n -= enemy[i]
            
        if n < 0:
            return i
    return i+1

print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
# 5
print(solution(2, 4, [3, 3, 3, 3]))
# 4
print(solution(20, 1, [3, 3, 3, 3]))

# 테스트 1 〉	통과 (0.29ms, 10.5MB)
# 테스트 2 〉	통과 (3.36ms, 11.3MB)
# 테스트 3 〉	통과 (260.26ms, 43MB)
# 테스트 4 〉	통과 (3.45ms, 18.4MB)
# 테스트 5 〉	통과 (0.07ms, 10.3MB)
# 테스트 6 〉	통과 (105.76ms, 53.2MB)
# 테스트 7 〉	통과 (80.25ms, 50.1MB)
# 테스트 8 〉	통과 (29.26ms, 49.4MB)
# 테스트 9 〉	통과 (50.36ms, 49.4MB)
# 테스트 10 〉	통과 (159.39ms, 45.7MB)
# 테스트 11 〉	통과 (0.02ms, 18.5MB)
# 테스트 12 〉	통과 (0.06ms, 18.4MB)
# 테스트 13 〉	통과 (0.00ms, 10.1MB)
# 테스트 14 〉	통과 (0.00ms, 10.1MB)
# 테스트 15 〉	통과 (0.01ms, 10.3MB)
# 테스트 16 〉	통과 (0.02ms, 10.1MB)
# 테스트 17 〉	통과 (0.00ms, 10.2MB)
# 테스트 18 〉	통과 (0.00ms, 10.1MB)
# 테스트 19 〉	통과 (0.00ms, 10MB)
# 테스트 20 〉	통과 (0.00ms, 10.3MB)
# 테스트 21 〉	통과 (0.01ms, 10.1MB)
# 테스트 22 〉	통과 (0.00ms, 10.1MB)
# 테스트 23 〉	통과 (0.02ms, 10.2MB)
# 테스트 24 〉	통과 (0.02ms, 10.2MB)
# 테스트 25 〉	통과 (0.04ms, 10.1MB)
# 테스트 26 〉	통과 (0.03ms, 10.2MB)
# 테스트 27 〉	통과 (0.06ms, 10.2MB)
# 테스트 28 〉	통과 (0.01ms, 10.2MB)
# 테스트 29 〉	통과 (0.05ms, 10.1MB)
# 테스트 30 〉	통과 (0.02ms, 10.1MB)
# 테스트 31 〉	통과 (0.04ms, 10.2MB)
# 테스트 32 〉	통과 (0.03ms, 10.2MB)