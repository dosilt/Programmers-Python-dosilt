# https://school.programmers.co.kr/learn/courses/30/lessons/181187

def calc(r, check=False):
    cnt = 0
    for y in range(r):
        x = (r**2 - y**2)**0.5
        if int(x) == x and check:
            cnt -= 1
        cnt += int(x)
    return cnt
    
def solution(r1, r2):
    a = calc(r1, True)
    b = calc(r2)
    return (b - a) * 4

print(solution(2, 3))
# 20
print(solution(10, 20))
# 952


# 테스트 1 〉	통과 (0.02ms, 10.1MB)
# 테스트 2 〉	통과 (0.06ms, 10.1MB)
# 테스트 3 〉	통과 (0.04ms, 10.1MB)
# 테스트 4 〉	통과 (2.11ms, 10.2MB)
# 테스트 5 〉	통과 (1.42ms, 10.2MB)
# 테스트 6 〉	통과 (2.60ms, 10.1MB)
# 테스트 7 〉	통과 (586.35ms, 10.3MB)
# 테스트 8 〉	통과 (1174.51ms, 10.2MB)
# 테스트 9 〉	통과 (616.73ms, 10.2MB)
# 테스트 10 〉	통과 (870.57ms, 10.2MB)