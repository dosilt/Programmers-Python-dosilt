# https://school.programmers.co.kr/learn/courses/30/lessons/138477

import heapq

def solution(k, score):
    answer = []
    result = []
    for s in score:
        heapq.heappush(result, s)
        if len(result) > k:
            heapq.heappop(result)
        answer.append(result[0])
    return answer

print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
# [10, 10, 10, 20, 20, 100, 100]
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))
# [0, 0, 0, 0, 20, 40, 70, 70, 150, 300]

# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.1MB)
# 테스트 6 〉	통과 (0.01ms, 10.3MB)
# 테스트 7 〉	통과 (0.01ms, 10.1MB)
# 테스트 8 〉	통과 (0.01ms, 10.3MB)
# 테스트 9 〉	통과 (0.01ms, 10.2MB)
# 테스트 10 〉	통과 (0.02ms, 10.3MB)
# 테스트 11 〉	통과 (0.02ms, 10.3MB)
# 테스트 12 〉	통과 (0.20ms, 10.2MB)
# 테스트 13 〉	통과 (0.36ms, 10.3MB)
# 테스트 14 〉	통과 (0.20ms, 10.4MB)
# 테스트 15 〉	통과 (0.44ms, 10.3MB)
# 테스트 16 〉	통과 (0.45ms, 10.2MB)
# 테스트 17 〉	통과 (0.47ms, 10.3MB)
# 테스트 18 〉	통과 (0.44ms, 10.3MB)
# 테스트 19 〉	통과 (0.34ms, 10.4MB)
# 테스트 20 〉	통과 (0.35ms, 10.4MB)
# 테스트 21 〉	통과 (0.36ms, 10.3MB)
# 테스트 22 〉	통과 (0.37ms, 10.3MB)
# 테스트 23 〉	통과 (0.40ms, 10.2MB)
# 테스트 24 〉	통과 (0.35ms, 10.3MB)
# 테스트 25 〉	통과 (0.38ms, 10.3MB)
# 테스트 26 〉	통과 (0.01ms, 10.2MB)