# https://school.programmers.co.kr/learn/courses/30/lessons/155652

def solution(s, skip, index):
    skip = set(list(skip))
    n = 0
    alpha2num, num2alpha = {}, {}
    for i in range(ord('z') - ord('a')+1):
        if chr(ord('a') + i) in skip:
            continue
        alpha2num[chr(ord('a') + i)] = n
        num2alpha[n] = chr(ord('a') + i)
        n += 1
        
    answer = ''
    for alpha in s:
        answer += num2alpha[(alpha2num[alpha] + index) % len(alpha2num)]
    return answer
        

print(solution("aukks", "wbqqd", 5))
# happy

# 테스트 1 〉	통과 (0.04ms, 10.3MB)
# 테스트 2 〉	통과 (0.02ms, 10.4MB)
# 테스트 3 〉	통과 (0.02ms, 10.2MB)
# 테스트 4 〉	통과 (0.02ms, 10MB)
# 테스트 5 〉	통과 (0.02ms, 10.4MB)
# 테스트 6 〉	통과 (0.04ms, 10.3MB)
# 테스트 7 〉	통과 (0.03ms, 10.1MB)
# 테스트 8 〉	통과 (0.03ms, 10.1MB)
# 테스트 9 〉	통과 (0.02ms, 10.4MB)
# 테스트 10 〉	통과 (0.02ms, 10.1MB)
# 테스트 11 〉	통과 (0.03ms, 10.4MB)
# 테스트 12 〉	통과 (0.05ms, 10.2MB)
# 테스트 13 〉	통과 (0.03ms, 10.3MB)
# 테스트 14 〉	통과 (0.02ms, 10.1MB)
# 테스트 15 〉	통과 (0.04ms, 10.2MB)
# 테스트 16 〉	통과 (0.03ms, 10.3MB)
# 테스트 17 〉	통과 (0.03ms, 10.2MB)
# 테스트 18 〉	통과 (0.04ms, 10.2MB)
# 테스트 19 〉	통과 (0.02ms, 10.2MB)