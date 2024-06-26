# https://school.programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    if x % sum(list(map(int, list(str(x))))) == 0:
        return True
    return False

print(solution(10))
# true
print(solution(12))
# true
print(solution(11))
# false
print(solution(13))
# false


# 테스트 1 〉	통과 (0.02ms, 10.5MB)
# 테스트 2 〉	통과 (0.02ms, 10.3MB)
# 테스트 3 〉	통과 (0.02ms, 10.4MB)
# 테스트 4 〉	통과 (0.03ms, 10.2MB)
# 테스트 5 〉	통과 (0.02ms, 10.3MB)
# 테스트 6 〉	통과 (0.02ms, 10.5MB)
# 테스트 7 〉	통과 (0.02ms, 10.3MB)
# 테스트 8 〉	통과 (0.02ms, 10.4MB)
# 테스트 9 〉	통과 (0.03ms, 10.4MB)
# 테스트 10 〉	통과 (0.02ms, 10.4MB)
# 테스트 11 〉	통과 (0.02ms, 10.2MB)
# 테스트 12 〉	통과 (0.02ms, 10.3MB)
# 테스트 13 〉	통과 (0.02ms, 10.3MB)
# 테스트 14 〉	통과 (0.03ms, 10.2MB)
# 테스트 15 〉	통과 (0.02ms, 10.4MB)
# 테스트 16 〉	통과 (0.02ms, 10.3MB)
# 테스트 17 〉	통과 (0.02ms, 10.4MB)