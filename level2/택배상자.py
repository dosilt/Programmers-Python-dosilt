# https://school.programmers.co.kr/learn/courses/30/lessons/131704

from collections import deque

def solution(order):
    queue = deque([])
    boxes = deque([n for n in range(1, len(order)+1)])
    
    answer = 0
    for o in order:
        if queue and queue[-1] == o:
            queue.pop()
            answer += 1
            continue
            
        while boxes and boxes[0] != o:
            queue.append(boxes.popleft())
        
        if boxes and boxes[0] == o:
            answer += 1
            boxes.popleft()
            continue
            
        break
            
    return answer

print(solution([4, 3, 1, 2, 5]))
# 2
print(solution([5, 4, 3, 2, 1]))
# 5

# 테스트 1 〉	통과 (19.96ms, 19.7MB)
# 테스트 2 〉	통과 (89.06ms, 53.5MB)
# 테스트 3 〉	통과 (116.22ms, 66.4MB)
# 테스트 4 〉	통과 (82.87ms, 50.1MB)
# 테스트 5 〉	통과 (176.99ms, 95.3MB)
# 테스트 6 〉	통과 (62.61ms, 28.5MB)
# 테스트 7 〉	통과 (250.84ms, 82.4MB)
# 테스트 8 〉	통과 (12.89ms, 13.8MB)
# 테스트 9 〉	통과 (164.10ms, 60MB)
# 테스트 10 〉	통과 (284.84ms, 95.4MB)