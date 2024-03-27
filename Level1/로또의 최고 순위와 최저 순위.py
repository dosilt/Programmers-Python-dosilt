# https://school.programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    win_nums = set(win_nums)
    answer = [0, 0]
    for lotto in lottos:
        if lotto == 0:
            answer[0] += 1
        elif lotto in win_nums:
            answer[0] += 1
            answer[1] += 1
            
    rank = {6:1, 5:2, 4:3, 3:4, 2:5}
    
    answer[0] = rank[answer[0]] if answer[0] > 1 else 6
    answer[1] = rank[answer[1]] if answer[1] > 1 else 6
    return answer
    
    

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
# [3, 5]
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
# [1, 6]
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))
# [1, 1]

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.00ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.00ms, 10.3MB)
# 테스트 8 〉	통과 (0.00ms, 10.3MB)
# 테스트 9 〉	통과 (0.00ms, 10.2MB)
# 테스트 10 〉	통과 (0.01ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
# 테스트 12 〉	통과 (0.01ms, 10.2MB)
# 테스트 13 〉	통과 (0.01ms, 10.2MB)
# 테스트 14 〉	통과 (0.01ms, 10.2MB)
# 테스트 15 〉	통과 (0.01ms, 10.2MB)