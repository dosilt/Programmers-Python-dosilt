# https://school.programmers.co.kr/learn/courses/30/lessons/178870

from collections import deque

def solution(sequence, k):
    queue = deque()
    cur_idx = 0
    answer = []
    summation = 0
    
    for n, seq in enumerate(sequence):
        queue.append(seq)
        summation += seq

        while queue and summation > k:
            temp = queue.popleft()
            cur_idx += 1
            summation -= temp

        if summation == k:
            answer.append([cur_idx, n, n-cur_idx])

    answer = sorted(answer, key=lambda x:[x[2], x[0]])
    
    return answer[0][:2]

print(solution([1, 2, 3, 4, 5], 7))
# [2, 3]
print(solution([1, 1, 1, 2, 3, 4, 5], 5))
# [6, 6]
print(solution([2, 2, 2, 2, 2], 6))
# [0, 2]


# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.4MB)
# 테스트 3 〉	통과 (0.03ms, 10.2MB)
# 테스트 4 〉	통과 (0.44ms, 10.1MB)
# 테스트 5 〉	통과 (2.68ms, 10.5MB)
# 테스트 6 〉	통과 (6.86ms, 10.8MB)
# 테스트 7 〉	통과 (14.48ms, 11.7MB)
# 테스트 8 〉	통과 (25.22ms, 13.3MB)
# 테스트 9 〉	통과 (63.99ms, 16.6MB)
# 테스트 10 〉	통과 (144.69ms, 26.9MB)
# 테스트 11 〉	통과 (287.62ms, 47.1MB)
# 테스트 12 〉	통과 (274.81ms, 46.1MB)
# 테스트 13 〉	통과 (259.46ms, 45.7MB)
# 테스트 14 〉	통과 (261.00ms, 45.3MB)
# 테스트 15 〉	통과 (259.27ms, 45.2MB)
# 테스트 16 〉	통과 (181.46ms, 56.7MB)
# 테스트 17 〉	통과 (1783.44ms, 309MB)
# 테스트 18 〉	통과 (0.03ms, 10.2MB)
# 테스트 19 〉	통과 (0.01ms, 10.1MB)
# 테스트 20 〉	통과 (0.01ms, 10.4MB)
# 테스트 21 〉	통과 (0.01ms, 10.3MB)
# 테스트 22 〉	통과 (0.02ms, 10.3MB)
# 테스트 23 〉	통과 (0.01ms, 10.2MB)
# 테스트 24 〉	통과 (1003.30ms, 166MB)
# 테스트 25 〉	통과 (151.42ms, 25.6MB)
# 테스트 26 〉	통과 (248.60ms, 18.5MB)
# 테스트 27 〉	통과 (267.11ms, 18.7MB)
# 테스트 28 〉	통과 (215.97ms, 21.7MB)
# 테스트 29 〉	통과 (237.00ms, 21.6MB)
# 테스트 30 〉	통과 (258.82ms, 51.3MB)
# 테스트 31 〉	통과 (0.01ms, 10.3MB)
# 테스트 32 〉	통과 (0.01ms, 10.2MB)
# 테스트 33 〉	통과 (0.02ms, 10.2MB)
# 테스트 34 〉	통과 (0.01ms, 10.2MB)