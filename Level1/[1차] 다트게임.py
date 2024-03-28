# https://school.programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    queue = [0]
    dartResult = dartResult.replace('10', 'A')
    cur_score = 0
    for dart in dartResult:
        if dart.isdigit():
            if cur_score != 0:
                queue.append(cur_score)
            cur_score = int(dart)
            
        elif dart == 'A':
            if cur_score != 0:
                queue.append(cur_score)
            cur_score = 10
            
        elif dart in ['S', 'D', 'T']:
            if dart == 'S':
                pass
            elif dart == 'D':
                cur_score = cur_score ** 2
            else:
                cur_score = cur_score ** 3    
            
        else: # "*", "#"
            if dart == '*':
                cur_score *= 2
                queue[-1] *= 2
            else:
                cur_score *= -1
    else:
        queue.append(cur_score)
        
    return sum(queue)

print(solution("1S2D*3T"))
# 37
print(solution("1D2S#10S"))
# 9
print(solution("1D2S0T"))
# 3
print(solution("1S*2T*3S"))
# 23
print(solution("1D#2S*3S"))
# 5
print(solution("1T2D3D#"))
# -4
print(solution("1D2S3T*"))
# 59


# 테스트 1 〉	통과 (0.03ms, 10.4MB)
# 테스트 2 〉	통과 (0.03ms, 10.5MB)
# 테스트 3 〉	통과 (0.04ms, 10.4MB)
# 테스트 4 〉	통과 (0.01ms, 10.4MB)
# 테스트 5 〉	통과 (0.03ms, 10.4MB)
# 테스트 6 〉	통과 (0.03ms, 10.4MB)
# 테스트 7 〉	통과 (0.03ms, 10.4MB)
# 테스트 8 〉	통과 (0.02ms, 10.4MB)
# 테스트 9 〉	통과 (0.03ms, 10.5MB)
# 테스트 10 〉	통과 (0.04ms, 10.4MB)
# 테스트 11 〉	통과 (0.02ms, 10.5MB)
# 테스트 12 〉	통과 (0.04ms, 10.4MB)
# 테스트 13 〉	통과 (0.03ms, 10.4MB)
# 테스트 14 〉	통과 (0.03ms, 10.5MB)
# 테스트 15 〉	통과 (0.03ms, 10.5MB)
# 테스트 16 〉	통과 (0.02ms, 10.5MB)
# 테스트 17 〉	통과 (0.03ms, 10.3MB)
# 테스트 18 〉	통과 (0.02ms, 10.5MB)
# 테스트 19 〉	통과 (0.02ms, 10.4MB)
# 테스트 20 〉	통과 (0.03ms, 10.3MB)
# 테스트 21 〉	통과 (0.02ms, 10.4MB)
# 테스트 22 〉	통과 (0.03ms, 10.4MB)
# 테스트 23 〉	통과 (0.02ms, 10.5MB)
# 테스트 24 〉	통과 (0.03ms, 10.3MB)
# 테스트 25 〉	통과 (0.03ms, 10.4MB)
# 테스트 26 〉	통과 (0.02ms, 10.4MB)
# 테스트 27 〉	통과 (0.02ms, 10.3MB)
# 테스트 28 〉	통과 (0.02ms, 10.4MB)
# 테스트 29 〉	통과 (0.02ms, 10.5MB)
# 테스트 30 〉	통과 (0.02ms, 10.5MB)
# 테스트 31 〉	통과 (0.03ms, 10.4MB)
# 테스트 32 〉	통과 (0.03ms, 10.4MB)