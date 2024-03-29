# https://school.programmers.co.kr/learn/courses/30/lessons/12977


def combination(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for n in combination(arr[i+1:], r-1):
                yield [arr[i]] + n


def even(n):
    temp = [False] + [True] * n
    
    for i in range(2, int(n**0.5)+1):
        idx, j = i, 2
        while idx * j < n + 1:
            temp[idx * j] = False
            j += 1
    return temp            



def solution(nums):
    candidates = [sum(x) for x in list(combination(nums, 3))]
    temp = even(max(candidates))
    answer = 0
    for candidate in candidates:
        if temp[candidate]:
            answer += 1
    return answer


print(solution([1, 2, 3, 4]))
# 1
print(solution([1, 2, 7, 6, 4]))
# 4

# 테스트 1 〉	통과 (2.17ms, 10.4MB)
# 테스트 2 〉	통과 (2.77ms, 10.4MB)
# 테스트 3 〉	통과 (0.78ms, 10.3MB)
# 테스트 4 〉	통과 (0.50ms, 10.3MB)
# 테스트 5 〉	통과 (3.30ms, 10.4MB)
# 테스트 6 〉	통과 (4.54ms, 10.6MB)
# 테스트 7 〉	통과 (0.50ms, 10.3MB)
# 테스트 8 〉	통과 (10.42ms, 11.8MB)
# 테스트 9 〉	통과 (1.17ms, 10.3MB)
# 테스트 10 〉	통과 (10.55ms, 11.7MB)
# 테스트 11 〉	통과 (0.13ms, 10.2MB)
# 테스트 12 〉	통과 (0.62ms, 10.4MB)
# 테스트 13 〉	통과 (0.15ms, 10.3MB)
# 테스트 14 〉	통과 (0.53ms, 10.4MB)
# 테스트 15 〉	통과 (0.14ms, 10.2MB)
# 테스트 16 〉	통과 (12.07ms, 12MB)
# 테스트 17 〉	통과 (24.11ms, 12.5MB)
# 테스트 18 〉	통과 (1.54ms, 10.3MB)
# 테스트 19 〉	통과 (1.39ms, 10.3MB)
# 테스트 20 〉	통과 (23.91ms, 12.6MB)
# 테스트 21 〉	통과 (25.18ms, 12.6MB)
# 테스트 22 〉	통과 (3.63ms, 10.5MB)
# 테스트 23 〉	통과 (0.03ms, 10.4MB)
# 테스트 24 〉	통과 (15.80ms, 11.9MB)
# 테스트 25 〉	통과 (13.58ms, 11.9MB)
# 테스트 26 〉	통과 (0.03ms, 10.2MB)