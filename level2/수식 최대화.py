# https://school.programmers.co.kr/learn/courses/30/lessons/67257

from collections import deque

def spliter(expression):
    temp = ''
    result = []
    for exp in expression:
        if exp.isdigit():
            temp += exp
        else:
            result.append(temp)
            result.append(exp)
            temp = ''
    else:
        result.append(temp)
    return deque([[result, []]])

def bfs(queue, candidates):
    result = 0
    while queue:
        d = queue.popleft()
        if len(d[1]) == 3:
            result = max(result, abs(d[0][0]))
            continue
        
        for i in range(3):
            temp = [d[0][0]]
            if i not in d[1]:
                cnt = 1
                while cnt < len(d[0]):
                    if d[0][cnt] == candidates[i]:
                        temp[-1] = eval(f'{temp[-1]}{candidates[i]}{d[0][cnt+1]}')
                        cnt += 2
                    else:
                        temp.append(d[0][cnt])
                        cnt += 1
                queue.append([temp, d[1] + [i]])
    return result
            
def solution(expression):
    candidates = ['+', '-', '*']
    
    queue = spliter(expression)
    answer = bfs(queue, candidates)
    return answer

print(solution("100-200*300-500+20"))
# 60420
print(solution("50*6-3*2"))
# 300

# 테스트 1 〉	통과 (0.15ms, 10.2MB)
# 테스트 2 〉	통과 (0.15ms, 10.3MB)
# 테스트 3 〉	통과 (0.40ms, 10.3MB)
# 테스트 4 〉	통과 (0.50ms, 10.2MB)
# 테스트 5 〉	통과 (0.64ms, 10.1MB)
# 테스트 6 〉	통과 (0.33ms, 10.4MB)
# 테스트 7 〉	통과 (0.50ms, 10.3MB)
# 테스트 8 〉	통과 (0.41ms, 10.4MB)
# 테스트 9 〉	통과 (0.75ms, 10.4MB)
# 테스트 10 〉	통과 (0.83ms, 10.3MB)
# 테스트 11 〉	통과 (0.48ms, 10.4MB)
# 테스트 12 〉	통과 (1.06ms, 10.2MB)
# 테스트 13 〉	통과 (0.69ms, 10.2MB)
# 테스트 14 〉	통과 (0.71ms, 10.3MB)
# 테스트 15 〉	통과 (0.91ms, 10.2MB)
# 테스트 16 〉	통과 (0.25ms, 10.2MB)
# 테스트 17 〉	통과 (0.29ms, 10.2MB)
# 테스트 18 〉	통과 (0.18ms, 10.3MB)
# 테스트 19 〉	통과 (0.17ms, 10.3MB)
# 테스트 20 〉	통과 (0.17ms, 10.2MB)
# 테스트 21 〉	통과 (0.92ms, 10.2MB)
# 테스트 22 〉	통과 (0.82ms, 10.3MB)
# 테스트 23 〉	통과 (0.21ms, 10.4MB)
# 테스트 24 〉	통과 (1.30ms, 10.3MB)
# 테스트 25 〉	통과 (1.21ms, 10.4MB)
# 테스트 26 〉	통과 (0.21ms, 10.2MB)
# 테스트 27 〉	통과 (0.77ms, 10.3MB)
# 테스트 28 〉	통과 (1.40ms, 10.3MB)
# 테스트 29 〉	통과 (0.81ms, 10.3MB)
# 테스트 30 〉	통과 (1.27ms, 10.2MB)