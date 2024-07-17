# https://school.programmers.co.kr/learn/courses/30/lessons/42883

from collections import deque

def solution(number, k):
    if len(number) - 1 == k:
        return max(number)
    
    answer = deque([int(number[0])])
    cnt = 0
    for idx, n in enumerate(number[1:]):
        while answer and int(n) > answer[-1]:
            answer.pop()
            cnt += 1
            if cnt == k:
                break
            
        answer.append(int(n))
            
        if cnt == k:
            answer = ''.join(list(map(str, answer))) + number[idx+2:]
            return answer
    
    if cnt != k:
        return ''.join(list(map(str, list(answer)[:-(k-cnt)])))

print(solution("9321", 1))

print(solution("1924", 2))
# 94
print(solution("1231234", 3))
# 3234
print(solution("4177252841", 4))
# 775841

# 테스트 1 〉	통과 (0.03ms, 10.4MB)
# 테스트 2 〉	통과 (0.04ms, 10.5MB)
# 테스트 3 〉	통과 (0.07ms, 10.3MB)
# 테스트 4 〉	통과 (0.15ms, 10.4MB)
# 테스트 5 〉	통과 (0.34ms, 10.4MB)
# 테스트 6 〉	통과 (7.07ms, 10.4MB)
# 테스트 7 〉	통과 (14.81ms, 10.6MB)
# 테스트 8 〉	통과 (37.82ms, 10.7MB)
# 테스트 9 〉	통과 (0.78ms, 11.6MB)
# 테스트 10 〉	통과 (202.48ms, 13.5MB)
# 테스트 11 〉	통과 (0.00ms, 10.2MB)
# 테스트 12 〉	통과 (0.03ms, 10.4MB)