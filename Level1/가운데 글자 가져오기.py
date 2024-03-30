# https://school.programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    length = len(s)
    return s[length//2] if length % 2 != 0 else s[length//2-1:length//2+1]

print(solution('abcde'))
# c
print(solution('qwer'))
# we

# 테스트 1 〉	통과 (0.00ms, 10.3MB)
# 테스트 2 〉	통과 (0.00ms, 10.3MB)
# 테스트 3 〉	통과 (0.00ms, 9.96MB)
# 테스트 4 〉	통과 (0.00ms, 10.2MB)
# 테스트 5 〉	통과 (0.00ms, 10.3MB)
# 테스트 6 〉	통과 (0.00ms, 10.1MB)
# 테스트 7 〉	통과 (0.00ms, 10.2MB)
# 테스트 8 〉	통과 (0.00ms, 10MB)
# 테스트 9 〉	통과 (0.00ms, 10.2MB)
# 테스트 10 〉	통과 (0.00ms, 9.97MB)
# 테스트 11 〉	통과 (0.00ms, 10.3MB)
# 테스트 12 〉	통과 (0.00ms, 10.1MB)
# 테스트 13 〉	통과 (0.00ms, 10.2MB)
# 테스트 14 〉	통과 (0.00ms, 10.1MB)
# 테스트 15 〉	통과 (0.00ms, 10MB)
# 테스트 16 〉	통과 (0.00ms, 10.1MB)