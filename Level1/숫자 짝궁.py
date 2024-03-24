# https://school.programmers.co.kr/learn/courses/30/lessons/131128

from collections import Counter

def solution(X, Y):
    x_cnt = Counter(X)
    y_cnt = Counter(Y)
    
    intersaction = []
    intersaction_key = set()
    length = 0
    for key in x_cnt.keys():
        if y_cnt[key] != 0:
            intersaction.extend([key] * min(y_cnt[key], x_cnt[key]))
            intersaction_key.add(key)
            length += 1
                
    if len(intersaction) == 0:
        return "-1"
    intersaction = sorted(intersaction, reverse=True)
    
    if length == 1 and '0' in intersaction_key:
        return "0"
    
    return "".join(intersaction)


print(solution("100", "2345"))
# -1
print(solution("100", "203045"))
# 0
print(solution("100", "123450"))
# 10
print(solution("12321", "42531"))
# 321
print(solution("5525", "1255"))
# 552


# 테스트 1 〉	통과 (0.03ms, 10.1MB)
# 테스트 2 〉	통과 (0.03ms, 10.2MB)
# 테스트 3 〉	통과 (0.03ms, 10.4MB)
# 테스트 4 〉	통과 (0.03ms, 10.1MB)
# 테스트 5 〉	통과 (0.03ms, 10.1MB)
# 테스트 6 〉	통과 (0.12ms, 10.2MB)
# 테스트 7 〉	통과 (0.08ms, 10.1MB)
# 테스트 8 〉	통과 (0.12ms, 10.2MB)
# 테스트 9 〉	통과 (0.08ms, 10.2MB)
# 테스트 10 〉	통과 (0.08ms, 10.3MB)
# 테스트 11 〉	통과 (431.66ms, 72.8MB)
# 테스트 12 〉	통과 (390.27ms, 70.6MB)
# 테스트 13 〉	통과 (395.12ms, 72.8MB)
# 테스트 14 〉	통과 (387.95ms, 70.5MB)
# 테스트 15 〉	통과 (447.71ms, 66MB)
# 테스트 16 〉	통과 (0.04ms, 10.2MB)
# 테스트 17 〉	통과 (0.03ms, 10.3MB)
# 테스트 18 〉	통과 (0.02ms, 10.3MB)
# 테스트 19 〉	통과 (0.03ms, 10.2MB)