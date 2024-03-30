# https://school.programmers.co.kr/learn/courses/30/lessons/12910


def solution(arr, divisor):
    answer = []
    for a in arr:
        if a % divisor == 0:
            answer.append(a)
    return sorted(answer) if answer else [-1]

print(solution([5, 9, 7, 10], 5))
# [5, 10]
print(solution([2, 36, 1, 3], 1))
# [1, 2, 3, 36]
print(solution([3,2,6], 10))
# [-1]

# 테스트 1 〉	통과 (0.01ms, 9.95MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.03ms, 10.2MB)
# 테스트 4 〉	통과 (0.02ms, 9.91MB)
# 테스트 5 〉	통과 (0.01ms, 10.3MB)
# 테스트 6 〉	통과 (3.48ms, 13.5MB)
# 테스트 7 〉	통과 (0.17ms, 10.3MB)
# 테스트 8 〉	통과 (0.00ms, 10.1MB)
# 테스트 9 〉	통과 (0.11ms, 10.2MB)
# 테스트 10 〉	통과 (0.08ms, 10.4MB)
# 테스트 11 〉	통과 (0.03ms, 10.2MB)
# 테스트 12 〉	통과 (0.07ms, 9.96MB)
# 테스트 13 〉	통과 (0.50ms, 10.3MB)
# 테스트 14 〉	통과 (0.11ms, 10.2MB)
# 테스트 15 〉	통과 (0.14ms, 10.3MB)
# 테스트 16 〉	통과 (0.03ms, 10.1MB)