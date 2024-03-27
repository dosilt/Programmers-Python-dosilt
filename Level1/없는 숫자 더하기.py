# https://school.programmers.co.kr/learn/courses/30/lessons/86051


def solution(numbers):
    candidate = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    return sum(candidate - set(numbers))

print(solution([1,2,3,4,6,7,8,0]))
# 14
print(solution([5,8,4,0,6,7,9]))
# 6

# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.1MB)
# 테스트 5 〉	통과 (0.01ms, 10.1MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.01ms, 10.3MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)
# 테스트 9 〉	통과 (0.01ms, 10.1MB)