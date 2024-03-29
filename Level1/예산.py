# https://school.programmers.co.kr/learn/courses/30/lessons/12982

import heapq

def solution(d, budget):
    heapq.heapify(d)
    answer = 0
    while d:
        temp = heapq.heappop(d)
        if temp <= budget:
            budget -= temp
            if budget >= 0:
                answer += 1
            else:
                return answer
    return answer

print(solution([1, 3, 2, 5, 4], 9))
# 3
print(solution([2, 2, 3, 3], 10))
# 4


# 테스트 1 〉	통과 (0.00ms, 10.2MB)
# 테스트 2 〉	통과 (0.00ms, 10.1MB)
# 테스트 3 〉	통과 (0.00ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.1MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.06ms, 10.2MB)
# 테스트 8 〉	통과 (0.06ms, 10.3MB)
# 테스트 9 〉	통과 (0.03ms, 10.2MB)
# 테스트 10 〉	통과 (0.03ms, 10MB)
# 테스트 11 〉	통과 (0.04ms, 10.3MB)
# 테스트 12 〉	통과 (0.06ms, 10.2MB)
# 테스트 13 〉	통과 (0.03ms, 10MB)
# 테스트 14 〉	통과 (0.05ms, 10.1MB)
# 테스트 15 〉	통과 (0.06ms, 10.2MB)
# 테스트 16 〉	통과 (0.06ms, 10.2MB)
# 테스트 17 〉	통과 (0.03ms, 10MB)
# 테스트 18 〉	통과 (0.06ms, 10.2MB)
# 테스트 19 〉	통과 (0.03ms, 10.2MB)
# 테스트 20 〉	통과 (0.05ms, 10.1MB)
# 테스트 21 〉	통과 (0.03ms, 10MB)
# 테스트 22 〉	통과 (0.04ms, 10.3MB)
# 테스트 23 〉	통과 (0.03ms, 10.2MB)