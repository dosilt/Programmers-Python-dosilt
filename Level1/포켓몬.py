# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    n = len(nums) // 2
    nums = list(set(nums))
    return min(n, len(nums))
    

print(solution([3, 1, 2, 3]))
# 2
print(solution([3, 3, 3, 2, 2, 4]))
# 3
print(solution([3, 3, 3, 2, 2, 2]))
# 2


# 테스트 1 〉	통과 (0.00ms, 10.2MB)
# 테스트 2 〉	통과 (0.00ms, 10.1MB)
# 테스트 3 〉	통과 (0.00ms, 10.1MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.00ms, 9.94MB)
# 테스트 6 〉	통과 (0.00ms, 10.3MB)
# 테스트 7 〉	통과 (0.01ms, 10.1MB)
# 테스트 8 〉	통과 (0.01ms, 10.1MB)
# 테스트 9 〉	통과 (0.01ms, 10.1MB)
# 테스트 10 〉	통과 (0.01ms, 9.93MB)
# 테스트 11 〉	통과 (0.01ms, 9.96MB)
# 테스트 12 〉	통과 (0.07ms, 10.2MB)
# 테스트 13 〉	통과 (0.06ms, 10.2MB)
# 테스트 14 〉	통과 (0.06ms, 10.1MB)
# 테스트 15 〉	통과 (0.04ms, 10.4MB)
# 테스트 16 〉	통과 (0.84ms, 11.1MB)
# 테스트 17 〉	통과 (0.43ms, 10.4MB)
# 테스트 18 〉	통과 (0.40ms, 10.5MB)
# 테스트 19 〉	통과 (0.31ms, 10.3MB)
# 테스트 20 〉	통과 (0.22ms, 10.4MB)