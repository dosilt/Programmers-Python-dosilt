# https://school.programmers.co.kr/learn/courses/30/lessons/12926

def logic(alpha, n):
    new_ord = ord(alpha) + n
    
    if ord('A') <= ord(alpha) <= ord('Z'):
        if new_ord > ord('Z'):
            new_ord = new_ord % ord('Z') + ord('A') - 1
    
    else:
        if new_ord > ord('z'):
            new_ord = new_ord % ord('z') + ord('a') - 1
            
    return chr(new_ord)
    
def solution(s, n):
    answer = ''
    for a in s:
        if a.isalpha():
            temp = logic(a, n)
            answer += temp
        else:
            answer += a
        
    return answer


print(solution("AB", 1))
# BC
print(solution("z", 1))
# a
print(solution("a B z", 4))
# e F d

# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.02ms, 10.1MB)
# 테스트 3 〉	통과 (0.03ms, 10.1MB)
# 테스트 4 〉	통과 (0.02ms, 10.2MB)
# 테스트 5 〉	통과 (0.02ms, 10.1MB)
# 테스트 6 〉	통과 (0.03ms, 10.2MB)
# 테스트 7 〉	통과 (0.02ms, 10.1MB)
# 테스트 8 〉	통과 (0.02ms, 10.1MB)
# 테스트 9 〉	통과 (0.04ms, 10.2MB)
# 테스트 10 〉	통과 (0.02ms, 10.2MB)
# 테스트 11 〉	통과 (0.05ms, 10.2MB)
# 테스트 12 〉	통과 (0.05ms, 10.1MB)
# 테스트 13 〉	통과 (4.98ms, 10.2MB)