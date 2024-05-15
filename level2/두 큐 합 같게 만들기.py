# https://school.programmers.co.kr/learn/courses/30/lessons/118667

from collections import deque

def solution(queue1, queue2):
    left_sum, right_sum = sum(queue1), sum(queue2)
    queue1, queue2 = deque(queue1), deque(queue2)
    
    length = len(queue1) + len(queue2) * 2
    
    answer = 0
    for i in range(length):
        if left_sum == right_sum:
            return i
        
        if left_sum >= right_sum and queue1:
            temp = queue1.popleft()
            queue2.append(temp)
            left_sum -= temp
            right_sum += temp
        else:
            temp = queue2.popleft()
            queue1.append(temp)
            right_sum -= temp
            left_sum += temp
    
    return answer if answer != 0 else -1

print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
# 2
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
# 7
print(solution([1, 1], [1, 5]))
# -1


# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 9.97MB)
# 테스트 5 〉	통과 (0.02ms, 10.2MB)
# 테스트 6 〉	통과 (0.05ms, 10.2MB)
# 테스트 7 〉	통과 (0.02ms, 10.2MB)
# 테스트 8 〉	통과 (0.03ms, 9.98MB)
# 테스트 9 〉	통과 (0.05ms, 10.3MB)
# 테스트 10 〉	통과 (0.21ms, 10.3MB)
# 테스트 11 〉	통과 (30.57ms, 14.6MB)
# 테스트 12 〉	통과 (5.85ms, 14.7MB)
# 테스트 13 〉	통과 (2.46ms, 12.1MB)
# 테스트 14 〉	통과 (2.80ms, 12.3MB)
# 테스트 15 〉	통과 (5.56ms, 18MB)
# 테스트 16 〉	통과 (3.82ms, 18.6MB)
# 테스트 17 〉	통과 (3.52ms, 17.6MB)
# 테스트 18 〉	통과 (11.20ms, 33.2MB)
# 테스트 19 〉	통과 (13.24ms, 37.2MB)
# 테스트 20 〉	통과 (28.05ms, 37.7MB)
# 테스트 21 〉	통과 (18.83ms, 37.9MB)
# 테스트 22 〉	통과 (54.01ms, 37.9MB)
# 테스트 23 〉	통과 (42.55ms, 38MB)
# 테스트 24 〉	통과 (65.67ms, 38.2MB)
# 테스트 25 〉	통과 (0.04ms, 10.2MB)
# 테스트 26 〉	통과 (0.05ms, 10.1MB)
# 테스트 27 〉	통과 (0.06ms, 10.1MB)
# 테스트 28 〉	통과 (64.01ms, 19.3MB)
# 테스트 29 〉	통과 (0.32ms, 11MB)
# 테스트 30 〉	통과 (44.99ms, 19.2MB)