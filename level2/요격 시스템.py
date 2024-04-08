# https://school.programmers.co.kr/learn/courses/30/lessons/181188

def solution(targets):
    targets = sorted(targets, key=lambda x:x[1])
    
    i = 0
    answer = 0
    while i < len(targets):
        answer += 1
        cur_time = targets[i][1]
        i += 1
        while i < len(targets) and cur_time > targets[i][0]:
            i += 1
    
    return answer

print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))
# 3

# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.03ms, 10.2MB)
# 테스트 3 〉	통과 (0.04ms, 10.2MB)
# 테스트 4 〉	통과 (0.47ms, 10.3MB)
# 테스트 5 〉	통과 (4.15ms, 11.6MB)
# 테스트 6 〉	통과 (59.93ms, 26.8MB)
# 테스트 7 〉	통과 (435.32ms, 94.9MB)
# 테스트 8 〉	통과 (414.45ms, 94.8MB)
# 테스트 9 〉	통과 (319.38ms, 81.2MB)
# 테스트 10 〉	통과 (95.67ms, 74.8MB)
# 테스트 11 〉	통과 (0.00ms, 9.98MB)