# https://school.programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    s = s.split('},{')
    if len(s) == 1:
        s[0] = s[0][2:-2]
        return [int(s[0])]
    else:
        s[0], s[-1] = s[0][2:], s[-1][:-2]
        
    s = sorted(s, key=lambda x:len(x))
    
    temp = []
    for i in s[1:]:
        temp.append(set(eval(i)))
    answer = [int(s[0])]
    
    t = list(temp[0] - {answer[0]})
    answer.append(t[0])
    
    for i in range(1, len(temp)):
        answer.append(list(temp[i] - temp[i-1])[0])
    
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
# [2, 1, 3, 4]
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
# [2, 1, 3, 4]
print(solution("{{20,111},{111}}"))
# [111, 20]
print(solution("{{123}}"))
# [123]
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
# [3, 2, 4, 1]

# 테스트 1 〉	통과 (0.07ms, 10.4MB)
# 테스트 2 〉	통과 (0.04ms, 10.3MB)
# 테스트 3 〉	통과 (0.02ms, 10.5MB)
# 테스트 4 〉	통과 (0.16ms, 10.3MB)
# 테스트 5 〉	통과 (1.06ms, 10.4MB)
# 테스트 6 〉	통과 (1.79ms, 10.4MB)
# 테스트 7 〉	통과 (20.43ms, 12.3MB)
# 테스트 8 〉	통과 (69.51ms, 16.1MB)
# 테스트 9 〉	통과 (29.28ms, 12.9MB)
# 테스트 10 〉	통과 (71.34ms, 16.5MB)
# 테스트 11 〉	통과 (86.61ms, 19.1MB)
# 테스트 12 〉	통과 (126.84ms, 23.8MB)
# 테스트 13 〉	통과 (134.70ms, 23.6MB)
# 테스트 14 〉	통과 (126.78ms, 23.9MB)
# 테스트 15 〉	통과 (0.02ms, 10.3MB)