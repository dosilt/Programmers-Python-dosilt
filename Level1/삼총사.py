# https://school.programmers.co.kr/learn/courses/30/lessons/131705

def combinations(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for j in combinations(arr[i+1:], r-1):
                yield [arr[i]] + j


def solution(number):
    answer = 0
    candidates = combinations(range(len(number)), 3)
    for candidate in candidates:
        summation = 0
        for c in candidate:
            summation += number[c]
        else:
            if summation == 0:
                answer += 1
    return answer


print(solution([-2, 3, 0, 2, -5]))
# 2
print(solution([-3, -2, -1, 0, 1, 2, 3]))
# 5
print(solution([-1, 1, -1, 1]))
# 0


# 테스트 1 〉	통과 (0.26ms, 10.1MB)
# 테스트 2 〉	통과 (0.05ms, 10.2MB)
# 테스트 3 〉	통과 (0.07ms, 10.2MB)
# 테스트 4 〉	통과 (0.12ms, 10.3MB)
# 테스트 5 〉	통과 (0.33ms, 10.2MB)
# 테스트 6 〉	통과 (0.22ms, 10.1MB)
# 테스트 7 〉	통과 (0.25ms, 10.1MB)
# 테스트 8 〉	통과 (0.26ms, 10.2MB)
# 테스트 9 〉	통과 (0.26ms, 10.1MB)
# 테스트 10 〉	통과 (0.28ms, 10.2MB)
# 테스트 11 〉	통과 (0.17ms, 10.1MB)
# 테스트 12 〉	통과 (0.20ms, 10.1MB)
# 테스트 13 〉	통과 (0.16ms, 10.2MB)