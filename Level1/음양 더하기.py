# https://school.programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    answer = 0
    for ab, si in zip(absolutes, signs):
        if si:
            answer += ab
        else:
            answer -= ab
    
    return answer

print(solution([4, 7, 12], [True, False, True]))
# 9
print(solution([1, 2, 3], [False, False, True]))
# 0


# 테스트 1 〉	통과 (0.05ms, 10.1MB)
# 테스트 2 〉	통과 (0.11ms, 10.2MB)
# 테스트 3 〉	통과 (0.06ms, 10.1MB)
# 테스트 4 〉	통과 (0.06ms, 10.2MB)
# 테스트 5 〉	통과 (0.06ms, 10.2MB)
# 테스트 6 〉	통과 (0.05ms, 10.1MB)
# 테스트 7 〉	통과 (0.09ms, 10.4MB)
# 테스트 8 〉	통과 (0.06ms, 10.1MB)
# 테스트 9 〉	통과 (0.06ms, 10.3MB)