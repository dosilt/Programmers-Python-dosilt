# https://school.programmers.co.kr/learn/courses/30/lessons/133502

from collections import deque

def check(queue, answer):
    if len(queue) >= 4 and queue[-2] == 3:
        for _ in range(4):
            queue.pop()
        answer += 1
        
    return queue, answer

def solution(ingredient):
    queue = deque([])
    answer = 0
    for i in ingredient:
        if i == 1:
            queue.append(i)
            queue, answer = check(queue, answer)
            
        elif queue and i == queue[-1] + 1:
            queue.append(i)
            
        else:
            queue = deque([])
            
    return answer

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
# 2 
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))
# 0
print(solution([1, 1, 2, 1, 2, 3, 1, 3, 1, 2, 3, 1]))
# 3

# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (62.77ms, 12.7MB)
# 테스트 4 〉	통과 (131.54ms, 15.6MB)
# 테스트 5 〉	통과 (169.52ms, 17.1MB)
# 테스트 6 〉	통과 (116.90ms, 13.9MB)
# 테스트 7 〉	통과 (119.75ms, 15.1MB)
# 테스트 8 〉	통과 (96.89ms, 14.2MB)
# 테스트 9 〉	통과 (82.07ms, 13.1MB)
# 테스트 10 〉	통과 (1.76ms, 10.2MB)
# 테스트 11 〉	통과 (63.82ms, 12.2MB)
# 테스트 12 〉	통과 (204.89ms, 18.6MB)
# 테스트 13 〉	통과 (0.00ms, 10.2MB)
# 테스트 14 〉	통과 (0.01ms, 10.2MB)
# 테스트 15 〉	통과 (0.01ms, 10.2MB)
# 테스트 16 〉	통과 (0.00ms, 10.4MB)
# 테스트 17 〉	통과 (0.01ms, 10.2MB)
# 테스트 18 〉	통과 (0.01ms, 10.3MB)