# https://school.programmers.co.kr/learn/courses/30/lessons/92342

from copy import deepcopy

def dfs(info, st, remain, cur_score, op_score, dummy):
    global answer
    if remain == 0:
        if cur_score > op_score:
            if answer == []:
                answer = [deepcopy(dummy), cur_score-op_score]
            else:
                if cur_score-op_score > answer[1]:
                    answer = [deepcopy(dummy), cur_score-op_score]
                elif cur_score-op_score == answer[1]:
                    for c in range(10, -1, -1):
                        if dummy[c] > answer[0][c]:
                            answer = [deepcopy(dummy), cur_score-op_score]
                        elif dummy[c] == answer[0][c]:
                            continue
                        else:
                            break
        return
    
    for i in range(st, 11):
        if info[i] < remain:
            dummy[i] = info[i] + 1
            temp = op_score - 10 + i if info[i] > 0 else op_score
            dfs(info, i+1, remain - info[i] - 1, cur_score + 10 - i, temp, dummy)
            dummy[i] = 0
        else:
            dummy[i] = remain
            dfs(info, i+1, 0, cur_score, op_score, dummy)
            dummy[i] = 0

def solution(n, info):
    global answer
    answer = []
    op_score = 0
    dummy = [0 for _ in range(11)]
    for i in range(11):
        if info[i] > 0:
            op_score += 10 - i
            
    dfs(info, 0, n, 0, op_score, dummy)
    return answer[0] if answer != [] else [-1]

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
# [0,2,2,0,1,0,0,0,0,0,0]
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
# [-1]
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
# [1,1,2,0,1,2,2,0,0,0,0]
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))
# [1,1,1,1,1,1,1,1,0,0,2]


# 테스트 1 〉	통과 (0.04ms, 10.2MB)
# 테스트 2 〉	통과 (0.54ms, 10.1MB)
# 테스트 3 〉	통과 (0.62ms, 10.2MB)
# 테스트 4 〉	통과 (0.26ms, 10.4MB)
# 테스트 5 〉	통과 (0.62ms, 10.1MB)
# 테스트 6 〉	통과 (0.59ms, 10.3MB)
# 테스트 7 〉	통과 (0.18ms, 10.2MB)
# 테스트 8 〉	통과 (0.11ms, 10.4MB)
# 테스트 9 〉	통과 (0.22ms, 10.2MB)
# 테스트 10 〉	통과 (0.08ms, 10.3MB)
# 테스트 11 〉	통과 (0.13ms, 10.2MB)
# 테스트 12 〉	통과 (0.14ms, 10.3MB)
# 테스트 13 〉	통과 (0.40ms, 10.2MB)
# 테스트 14 〉	통과 (0.55ms, 10.3MB)
# 테스트 15 〉	통과 (0.60ms, 10.3MB)
# 테스트 16 〉	통과 (0.31ms, 10.3MB)
# 테스트 17 〉	통과 (0.22ms, 10.1MB)
# 테스트 18 〉	통과 (0.04ms, 10.2MB)
# 테스트 19 〉	통과 (0.01ms, 10.2MB)
# 테스트 20 〉	통과 (0.64ms, 10.2MB)
# 테스트 21 〉	통과 (0.51ms, 10.3MB)
# 테스트 22 〉	통과 (0.72ms, 10.3MB)
# 테스트 23 〉	통과 (0.06ms, 10.1MB)
# 테스트 24 〉	통과 (0.81ms, 10.2MB)
# 테스트 25 〉	통과 (0.79ms, 10.3MB)