# https://school.programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    string = ''
    a = n
    while a != 0:
        a, b = divmod(n, 3)
        string += f'{b}'
        n = a

    answer = 0
    for n, i in enumerate(str(int(string))[::-1]):
        answer += int(i) * (3 ** n)
        
    return answer

print(solution(45))
# 7
print(solution(125))
# 229

# 테스트 1 〉	통과 (0.03ms, 10.3MB)
# 테스트 2 〉	통과 (0.04ms, 10.4MB)
# 테스트 3 〉	통과 (0.03ms, 10.3MB)
# 테스트 4 〉	통과 (0.02ms, 10.4MB)
# 테스트 5 〉	통과 (0.03ms, 10.5MB)
# 테스트 6 〉	통과 (0.04ms, 10.4MB)
# 테스트 7 〉	통과 (0.03ms, 10.2MB)
# 테스트 8 〉	통과 (0.02ms, 10.4MB)
# 테스트 9 〉	통과 (0.03ms, 10.4MB)
# 테스트 10 〉	통과 (0.04ms, 10.3MB)