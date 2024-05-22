# https://school.programmers.co.kr/learn/courses/30/lessons/60058

def step1(p):
    if p == '':
        return True, p
    return False, p

def step2_check(p):
    cnt = 0
    for i in p:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
        if cnt < 0:
            return False
    return True
            
def step2_spliter(p):
    cnt = 0
    for n, i in enumerate(p):
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
            
        if cnt == 0:
            return p[:n+1], p[n+1:]
    return p, ''
    
def flip(p):
    temp = ''
    for i in p:
        if i == '(':
            temp += ')'
        else:
            temp += '('
    return temp
    
def process(p):
    check, p = step1(p)
    if check:
        return p
    
    check = step2_check(p)
    if check:
        return p
    
    u, v = step2_spliter(p)
    if step2_check(u):
        v = process(v)
        return u+v
    else:
        v = '(' + process(v) + ')'
        u = flip(u[1:-1])
        return v + u

def solution(p):
    return process(p)


print(solution("(()())()"))
# "(()())()"
print(solution(")("))
# "()"
print(solution("()))((()"))
# "()(())()"

# 테스트 1 〉	통과 (0.00ms, 10.4MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.00ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.3MB)
# 테스트 5 〉	통과 (0.00ms, 10.3MB)
# 테스트 6 〉	통과 (0.01ms, 10.4MB)
# 테스트 7 〉	통과 (0.01ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.3MB)
# 테스트 9 〉	통과 (0.01ms, 10.4MB)
# 테스트 10 〉	통과 (0.02ms, 10.1MB)
# 테스트 11 〉	통과 (0.03ms, 10.3MB)
# 테스트 12 〉	통과 (0.03ms, 10.2MB)
# 테스트 13 〉	통과 (0.04ms, 10.4MB)
# 테스트 14 〉	통과 (0.07ms, 10.2MB)
# 테스트 15 〉	통과 (0.09ms, 10.2MB)
# 테스트 16 〉	통과 (0.29ms, 10.3MB)
# 테스트 17 〉	통과 (0.17ms, 10.1MB)
# 테스트 18 〉	통과 (0.64ms, 10.3MB)
# 테스트 19 〉	통과 (0.31ms, 10.3MB)
# 테스트 20 〉	통과 (0.41ms, 10.3MB)
# 테스트 21 〉	통과 (0.26ms, 10.2MB)
# 테스트 22 〉	통과 (0.23ms, 10.3MB)
# 테스트 23 〉	통과 (0.41ms, 10.2MB)
# 테스트 24 〉	통과 (0.12ms, 10.4MB)
# 테스트 25 〉	통과 (0.24ms, 10.3MB)