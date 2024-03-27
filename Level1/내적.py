# https://school.programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    return sum([a_*b_ for a_, b_ in zip(a, b)])

print(solution([1,2,3,4], [-3,-1,0,2]))
# 3
print(solution([-1,0,1], [1,0,-1]))
# -2

# 테스트 1 〉	통과 (0.08ms, 10.4MB)
# 테스트 2 〉	통과 (0.02ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.02ms, 10MB)
# 테스트 5 〉	통과 (0.01ms, 10.3MB)
# 테스트 6 〉	통과 (0.09ms, 10.3MB)
# 테스트 7 〉	통과 (0.08ms, 10.3MB)
# 테스트 8 〉	통과 (0.15ms, 10.2MB)
# 테스트 9 〉	통과 (0.13ms, 10.2MB)