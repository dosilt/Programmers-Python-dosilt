# https://school.programmers.co.kr/learn/courses/30/lessons/72410


def solution(new_id):
    # 소문자 치환
    new_id = new_id.lower()
    
    # 특수 문자 제거
    string = ''
    for new in new_id:
        if new.isalpha() or new.isdigit() or new in ['-', '_', '.']:
            string += new
    new_id = string
        
    # . 중복 제거
    string = ''
    for new in new_id:
        if new == '.':
            if string and string[-1] == '.':
                continue
        string += new
        
    # strip
    string = string.strip('.')
    print(string)
    
    # 비면 a 추가
    if len(string) == 0:
        string += 'a'
    
    if len(string) >= 16:
        string = string[:15].strip('.')
    
    while len(string) < 3:
        string += string[-1]
            
    answer = string            
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
# "bat.y.abcdefghi"
print(solution("z-+.^."))
# "z--"
print(solution(	"=.="))
# "aaa"
print(solution("123_.def"))
# "123_.def"
print(solution("abcdefghijklmn.p"))
# "abcdefghijklmn"

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.02ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.1MB)
# 테스트 6 〉	통과 (0.01ms, 10.1MB)
# 테스트 7 〉	통과 (0.01ms, 10.3MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)
# 테스트 9 〉	통과 (0.01ms, 10.1MB)
# 테스트 10 〉	통과 (0.01ms, 10.3MB)
# 테스트 11 〉	통과 (0.02ms, 10.1MB)
# 테스트 12 〉	통과 (0.02ms, 10.4MB)
# 테스트 13 〉	통과 (0.01ms, 10.1MB)
# 테스트 14 〉	통과 (0.01ms, 10.1MB)
# 테스트 15 〉	통과 (0.02ms, 10.3MB)
# 테스트 16 〉	통과 (0.05ms, 10.2MB)
# 테스트 17 〉	통과 (0.13ms, 10.3MB)
# 테스트 18 〉	통과 (0.20ms, 10.1MB)
# 테스트 19 〉	통과 (0.43ms, 10.2MB)
# 테스트 20 〉	통과 (0.30ms, 10.4MB)
# 테스트 21 〉	통과 (0.20ms, 10.3MB)
# 테스트 22 〉	통과 (0.16ms, 10.1MB)
# 테스트 23 〉	통과 (0.28ms, 10.1MB)
# 테스트 24 〉	통과 (0.22ms, 10.3MB)
# 테스트 25 〉	통과 (0.47ms, 10.2MB)
# 테스트 26 〉	통과 (0.25ms, 10.1MB)