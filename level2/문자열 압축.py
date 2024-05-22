# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def merging(arr, candidate):
    temp = [arr[:candidate]]
    cnt = [1]
    for i in range(candidate, len(arr), candidate):
        a = arr[i:i+candidate]
        if a == temp[-1]:
            cnt[-1] += 1
        else:
            temp.append(a)
            cnt.append(1)
            
    answer = ''
    for t, c in zip(temp, cnt):
        if c == 1:
            answer += t
        else:
            answer += f'{c}{t}'
    return len(answer)


def solution(s):
    if len(s) == 1:
        return 1
    
    answer = float('inf')
    for candidate in range(1, len(s)//2+1):
        answer = min(merging(s, candidate), answer)
    return answer

print(solution("aabbaccc"))
# 7
print(solution("ababcdcdababcdcd"))
# 9
print(solution("abcabcdede"))
# 8
print(solution("abcabcabcabcdededededede"))
# 14
print(solution("xababcdcdababcdcd"))
# 17

# 테스트 1 〉	통과 (0.05ms, 10.2MB)
# 테스트 2 〉	통과 (0.42ms, 10.2MB)
# 테스트 3 〉	통과 (0.24ms, 10.4MB)
# 테스트 4 〉	통과 (0.04ms, 10.1MB)
# 테스트 5 〉	통과 (0.00ms, 10.3MB)
# 테스트 6 〉	통과 (0.05ms, 10.2MB)
# 테스트 7 〉	통과 (1.01ms, 10.2MB)
# 테스트 8 〉	통과 (0.50ms, 10.3MB)
# 테스트 9 〉	통과 (0.72ms, 10.3MB)
# 테스트 10 〉	통과 (5.11ms, 10.2MB)
# 테스트 11 〉	통과 (0.19ms, 10.2MB)
# 테스트 12 〉	통과 (0.11ms, 10.1MB)
# 테스트 13 〉	통과 (0.13ms, 10.1MB)
# 테스트 14 〉	통과 (0.66ms, 10.2MB)
# 테스트 15 〉	통과 (0.13ms, 10.1MB)
# 테스트 16 〉	통과 (0.02ms, 10.3MB)
# 테스트 17 〉	통과 (1.52ms, 10.2MB)
# 테스트 18 〉	통과 (1.22ms, 10.4MB)
# 테스트 19 〉	통과 (1.28ms, 10.1MB)
# 테스트 20 〉	통과 (2.92ms, 10.3MB)
# 테스트 21 〉	통과 (2.90ms, 10.3MB)
# 테스트 22 〉	통과 (2.73ms, 10.2MB)
# 테스트 23 〉	통과 (2.80ms, 10.3MB)
# 테스트 24 〉	통과 (2.67ms, 10.3MB)
# 테스트 25 〉	통과 (2.92ms, 10.2MB)
# 테스트 26 〉	통과 (2.75ms, 10.4MB)
# 테스트 27 〉	통과 (2.92ms, 10.2MB)
# 테스트 28 〉	통과 (0.04ms, 10.2MB)