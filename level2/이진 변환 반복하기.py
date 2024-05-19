# https://school.programmers.co.kr/learn/courses/30/lessons/70129

from collections import Counter

def solution(s):
    # 변환, 지워진 개수
    answer = [0, 0]
    while True:
        if s == '1':
            break
        
        temp = Counter(s)
        s = bin(len(temp['1'] * '1'))[2:]
        answer[1] += temp['0']
        answer[0] += 1
    return answer

print(solution("110010101001"))
# [3, 8]
print(solution("01110"))
# [3, 3]
print(solution("1111111"))
# [4, 1]

# 테스트 1 〉	통과 (0.07ms, 10.3MB)
# 테스트 2 〉	통과 (7.31ms, 10.3MB)
# 테스트 3 〉	통과 (0.06ms, 10.1MB)
# 테스트 4 〉	통과 (0.04ms, 9.97MB)
# 테스트 5 〉	통과 (0.02ms, 10.1MB)
# 테스트 6 〉	통과 (0.12ms, 10.1MB)
# 테스트 7 〉	통과 (0.18ms, 10.2MB)
# 테스트 8 〉	통과 (0.10ms, 10MB)
# 테스트 9 〉	통과 (3.61ms, 10.1MB)
# 테스트 10 〉	통과 (9.53ms, 10.4MB)
# 테스트 11 〉	통과 (5.74ms, 10.2MB)