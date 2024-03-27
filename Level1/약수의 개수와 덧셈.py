# https://school.programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    temp = 0
    for i in range(int(left**0.5)+1, int(right**0.5)+1):
        temp += i ** 2 * 2
    answer = 0
    for i in range(left, right+1):
        answer += i
    return answer - temp if left != 1 else answer - temp - 2

# print(solution(13, 17))
# # 43
# print(solution(24, 27))
# # 52


# 테스트 1 〉	통과 (0.06ms, 10.4MB)
# 테스트 2 〉	통과 (0.03ms, 10.2MB)
# 테스트 3 〉	통과 (0.04ms, 10.2MB)
# 테스트 4 〉	통과 (0.02ms, 10.3MB)
# 테스트 5 〉	통과 (0.05ms, 10.3MB)
# 테스트 6 〉	통과 (0.02ms, 10.2MB)
# 테스트 7 〉	통과 (0.02ms, 10.2MB)