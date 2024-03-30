# https://school.programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    num = sorted(list(str(n)), key=lambda x:x[0], reverse=True)
    return int(''.join(num))


print(solution(118372))
# 873211

# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.02ms, 10.4MB)
# 테스트 3 〉	통과 (0.02ms, 10.3MB)
# 테스트 4 〉	통과 (0.02ms, 10.3MB)
# 테스트 5 〉	통과 (0.03ms, 10.2MB)
# 테스트 6 〉	통과 (0.03ms, 10.3MB)
# 테스트 7 〉	통과 (0.02ms, 10.2MB)
# 테스트 8 〉	통과 (0.03ms, 10.2MB)
# 테스트 9 〉	통과 (0.02ms, 10.3MB)
# 테스트 10 〉	통과 (0.03ms, 10.1MB)
# 테스트 11 〉	통과 (0.02ms, 10.2MB)
# 테스트 12 〉	통과 (0.02ms, 10.4MB)
# 테스트 13 〉	통과 (0.03ms, 10.2MB)
# 테스트 14 〉	통과 (0.02ms, 10.4MB)
# 테스트 15 〉	통과 (0.02ms, 10.4MB)
# 테스트 16 〉	통과 (0.02ms, 10.2MB)