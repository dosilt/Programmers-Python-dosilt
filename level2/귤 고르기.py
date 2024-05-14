# https://school.programmers.co.kr/learn/courses/30/lessons/138476

from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)
    for i, (_, x) in enumerate(counter.most_common()):
        if k - x <= 0:
            return i+1
        k -= x
    return len(counter.keys())

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
# 3
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))
# 2
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))
# 1

# 테스트 1 〉	통과 (6.60ms, 13.1MB)
# 테스트 2 〉	통과 (6.39ms, 13.1MB)
# 테스트 3 〉	통과 (8.22ms, 13.2MB)
# 테스트 4 〉	통과 (7.08ms, 13.1MB)
# 테스트 5 〉	통과 (5.37ms, 11.1MB)
# 테스트 6 〉	통과 (10.51ms, 11.4MB)
# 테스트 7 〉	통과 (6.93ms, 12.6MB)
# 테스트 8 〉	통과 (6.39ms, 11.9MB)
# 테스트 9 〉	통과 (5.84ms, 11.6MB)
# 테스트 10 〉	통과 (6.96ms, 12.9MB)
# 테스트 11 〉	통과 (0.05ms, 10.2MB)
# 테스트 12 〉	통과 (0.02ms, 10.2MB)
# 테스트 13 〉	통과 (0.02ms, 10.1MB)
# 테스트 14 〉	통과 (0.02ms, 10MB)
# 테스트 15 〉	통과 (0.04ms, 10.3MB)
# 테스트 16 〉	통과 (0.02ms, 10.2MB)
# 테스트 17 〉	통과 (0.04ms, 10.1MB)
# 테스트 18 〉	통과 (0.02ms, 10.1MB)
# 테스트 19 〉	통과 (0.02ms, 10.3MB)
# 테스트 20 〉	통과 (0.03ms, 10.1MB)
# 테스트 21 〉	통과 (0.13ms, 10.1MB)
# 테스트 22 〉	통과 (0.39ms, 10.3MB)
# 테스트 23 〉	통과 (0.27ms, 10.3MB)
# 테스트 24 〉	통과 (0.26ms, 10.3MB)
# 테스트 25 〉	통과 (3.09ms, 11.2MB)
# 테스트 26 〉	통과 (5.04ms, 12.5MB)
# 테스트 27 〉	통과 (41.54ms, 26.4MB)
# 테스트 28 〉	통과 (23.85ms, 18.5MB)
# 테스트 29 〉	통과 (31.96ms, 21.2MB)
# 테스트 30 〉	통과 (41.70ms, 26.4MB)
# 테스트 31 〉	통과 (6.77ms, 12.6MB)
# 테스트 32 〉	통과 (7.42ms, 13.8MB)
# 테스트 33 〉	통과 (30.44ms, 22.2MB)
# 테스트 34 〉	통과 (25.85ms, 21.4MB)