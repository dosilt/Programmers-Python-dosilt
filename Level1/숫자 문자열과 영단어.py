# https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    s = s.replace('zero', '0')
    s = s.replace('one', '1')
    s = s.replace('two', '2')
    s = s.replace('three', '3')
    s = s.replace('four', '4')
    s = s.replace('five', '5')
    s = s.replace('six', '6')
    s = s.replace('seven', '7')
    s = s.replace('eight', '8')
    s = s.replace('nine', '9')
    return int(s)

print(solution("one4seveneight"))
# 1478
print(solution("23four5six7"))
# 234567
print(solution("2three45sixseven"))
# 234567
print(solution("123"))
# 123

# 테스트 1 〉	통과 (0.02ms, 10.5MB)
# 테스트 2 〉	통과 (0.02ms, 10.5MB)
# 테스트 3 〉	통과 (0.02ms, 10.5MB)
# 테스트 4 〉	통과 (0.02ms, 10.4MB)
# 테스트 5 〉	통과 (0.02ms, 10.5MB)
# 테스트 6 〉	통과 (0.03ms, 10.3MB)
# 테스트 7 〉	통과 (0.02ms, 10.3MB)
# 테스트 8 〉	통과 (0.02ms, 10.5MB)
# 테스트 9 〉	통과 (0.03ms, 10.4MB)
# 테스트 10 〉	통과 (0.02ms, 10.3MB)