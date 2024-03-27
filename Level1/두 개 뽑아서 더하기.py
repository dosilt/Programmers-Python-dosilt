# https://school.programmers.co.kr/learn/courses/30/lessons/68644

def combinations(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for n in combinations(arr[i+1:], r-1):
                yield [arr[i]] + n


def solution(numbers):
    combi = list(combinations(numbers, 2))
    answer = set()
    for com in combi:
        answer.add(sum(com))
    return sorted(list(answer))

print(solution([2, 1, 3, 4, 1]))
# [2, 3, 4, 5, 6, 7]
print(solution([5, 0, 2, 7]))
# [2, 5, 7, 9, 12]

# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.02ms, 10.2MB)
# 테스트 3 〉	통과 (0.02ms, 10.1MB)
# 테스트 4 〉	통과 (0.02ms, 10.3MB)
# 테스트 5 〉	통과 (0.04ms, 10.2MB)
# 테스트 6 〉	통과 (0.08ms, 10.3MB)
# 테스트 7 〉	통과 (1.93ms, 10.3MB)
# 테스트 8 〉	통과 (2.13ms, 10.4MB)
# 테스트 9 〉	통과 (3.94ms, 10.5MB)