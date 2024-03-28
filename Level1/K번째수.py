# https://school.programmers.co.kr/learn/courses/30/lessons/42748


def solution(array, commands):
    answer = []
    for st, en, idx in commands:
        answer.append(sorted(array[st-1:en])[idx-1])
    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
# [5, 6, 3]


# 테스트 1 〉	통과 (0.00ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.00ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.1MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.00ms, 10.2MB)
# 테스트 7 〉	통과 (0.01ms, 10.2MB)