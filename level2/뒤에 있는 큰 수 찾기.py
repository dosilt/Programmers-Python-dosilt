# https://school.programmers.co.kr/learn/courses/30/lessons/154539

from collections import deque

def solution(numbers):
    answer = [-1] * len(numbers)
    queue = deque()
    for n, num in enumerate(numbers):
        if n == 0:
            queue.append([n, num])
        else:
            while queue and num > queue[-1][1]:
                i, c = queue.pop()
                answer[i] = num
            queue.append([n, num])
    return answer

print(solution([2, 3, 3, 5]))
# [3, 5, 5, -1]
print(solution([9, 1, 5, 3, 6, 2]))
# [-1, 5, 6, 6, -1, -1]


# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.03ms, 10.1MB)
# 테스트 5 〉	통과 (0.65ms, 10.4MB)
# 테스트 6 〉	통과 (3.22ms, 11.3MB)
# 테스트 7 〉	통과 (3.16ms, 11.4MB)
# 테스트 8 〉	통과 (15.94ms, 17.1MB)
# 테스트 9 〉	통과 (15.78ms, 17.1MB)
# 테스트 10 〉	통과 (33.81ms, 19.7MB)
# 테스트 11 〉	통과 (31.92ms, 19.6MB)
# 테스트 12 〉	통과 (65.82ms, 25.4MB)
# 테스트 13 〉	통과 (72.14ms, 25.4MB)
# 테스트 14 〉	통과 (169.28ms, 43.3MB)
# 테스트 15 〉	통과 (321.13ms, 75.4MB)
# 테스트 16 〉	통과 (335.46ms, 75.4MB)
# 테스트 17 〉	통과 (331.15ms, 75.5MB)
# 테스트 18 〉	통과 (322.06ms, 75.5MB)
# 테스트 19 〉	통과 (358.39ms, 75.5MB)
# 테스트 20 〉	통과 (831.31ms, 149MB)
# 테스트 21 〉	통과 (726.54ms, 180MB)
# 테스트 22 〉	통과 (459.15ms, 75MB)
# 테스트 23 〉	통과 (774.24ms, 180MB)