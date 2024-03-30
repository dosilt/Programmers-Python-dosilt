# https://school.programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    answer = []
    words = s.split(' ')
    
    for word in words:
        temp = ''
        for n, a in enumerate(word):
            temp += a.upper() if n % 2 == 0 else a.lower()
        answer.append(temp)
    return ' '.join(answer)


print(solution("try hello world"))
# "TrY HeLlO WoRlD"


# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 9.93MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.08ms, 10MB)
# 테스트 5 〉	통과 (0.02ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.1MB)
# 테스트 7 〉	통과 (0.01ms, 10.1MB)
# 테스트 8 〉	통과 (0.03ms, 10.1MB)
# 테스트 9 〉	통과 (0.04ms, 9.95MB)
# 테스트 10 〉	통과 (0.03ms, 10.1MB)
# 테스트 11 〉	통과 (0.04ms, 10.1MB)
# 테스트 12 〉	통과 (0.04ms, 10.1MB)
# 테스트 13 〉	통과 (0.02ms, 10.3MB)
# 테스트 14 〉	통과 (0.01ms, 10.3MB)
# 테스트 15 〉	통과 (0.02ms, 10.3MB)
# 테스트 16 〉	통과 (0.02ms, 10.1MB)