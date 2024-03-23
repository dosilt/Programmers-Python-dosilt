# https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    temp = ['', 0, 0]
    answer = 0
    result = ''
    for alpha in s:
        if temp[0] == '':
            temp[0] = alpha
            temp[1] += 1
            result += alpha
        else:
            if temp[0] == alpha:
                temp[1] += 1
            else:
                temp[2] += 1
                
            result += alpha
            
            if temp[1] == temp[2]:
                answer += 1
                result = ''
                temp = ['', 0, 0]
    if temp[0] != '':
        return answer + 1
    return answer

print(solution("banana"))
# 3
print(solution("abracadabra"))
# 6
print(solution("aaabbaccccabba"))
# 3


# 테스트 1 〉	통과 (0.00ms, 10.3MB)
# 테스트 2 〉	통과 (0.78ms, 10.4MB)
# 테스트 3 〉	통과 (1.52ms, 10.4MB)
# 테스트 4 〉	통과 (0.00ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.3MB)
# 테스트 6 〉	통과 (0.00ms, 10.2MB)
# 테스트 7 〉	통과 (0.00ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.4MB)
# 테스트 9 〉	통과 (1.04ms, 10.2MB)
# 테스트 10 〉	통과 (2.29ms, 10.2MB)
# 테스트 11 〉	통과 (0.69ms, 10.1MB)
# 테스트 12 〉	통과 (1.82ms, 10.3MB)
# 테스트 13 〉	통과 (1.83ms, 10.2MB)
# 테스트 14 〉	통과 (1.93ms, 10.2MB)
# 테스트 15 〉	통과 (0.60ms, 10.4MB)
# 테스트 16 〉	통과 (2.10ms, 10.3MB)
# 테스트 17 〉	통과 (0.69ms, 10.3MB)
# 테스트 18 〉	통과 (1.62ms, 10.4MB)
# 테스트 19 〉	통과 (1.74ms, 10.2MB)
# 테스트 20 〉	통과 (1.55ms, 10.3MB)
# 테스트 21 〉	통과 (3.00ms, 10.4MB)
# 테스트 22 〉	통과 (2.00ms, 10.1MB)
# 테스트 23 〉	통과 (0.39ms, 10.1MB)
# 테스트 24 〉	통과 (1.00ms, 10.3MB)
# 테스트 25 〉	통과 (1.85ms, 10.2MB)
# 테스트 26 〉	통과 (2.61ms, 10.2MB)
# 테스트 27 〉	통과 (1.27ms, 10.3MB)
# 테스트 28 〉	통과 (1.41ms, 10.2MB)
# 테스트 29 〉	통과 (1.69ms, 10.2MB)
# 테스트 30 〉	통과 (1.79ms, 10.2MB)
# 테스트 31 〉	통과 (0.00ms, 10.2MB)
# 테스트 32 〉	통과 (0.00ms, 10.3MB)
# 테스트 33 〉	통과 (0.00ms, 10.2MB)
# 테스트 34 〉	통과 (0.00ms, 10.3MB)
# 테스트 35 〉	통과 (0.01ms, 10.1MB)
# 테스트 36 〉	통과 (0.01ms, 10.3MB)
# 테스트 37 〉	통과 (0.01ms, 10.2MB)
# 테스트 38 〉	통과 (0.01ms, 10.2MB)
# 테스트 39 〉	통과 (0.01ms, 10.4MB)
# 테스트 40 〉	통과 (0.02ms, 10.4MB)
# 테스트 41 〉	통과 (1.84ms, 10.2MB)
# 테스트 42 〉	통과 (1.81ms, 10.4MB)