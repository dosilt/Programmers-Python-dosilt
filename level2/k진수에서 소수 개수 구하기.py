# https://school.programmers.co.kr/learn/courses/30/lessons/92335#qna

def convert(n, k):
    temp = ''
    while n > k:
        n, b = divmod(n, k)
        temp = str(b) + temp
    temp = str(n) + temp
    candidates = [int(x) for x in temp.split('0') if x > '1']
    return candidates

def prime_find(value):
    for i in range(2, int(value**0.5)+1):
        if value % i == 0:
            return 0
    return 1
    
def solution(n, k):
    candidates = convert(n, k)
    if candidates == []:
        return 0
    answer = 0
    for candidate in candidates:
        temp = prime_find(candidate)
        answer += temp
    return answer

print(solution(437674, 3))
# 3
print(solution(110011, 10))
# 2

# 테스트 1 〉	통과 (107.34ms, 10.4MB)
# 테스트 2 〉	통과 (0.04ms, 10.5MB)
# 테스트 3 〉	통과 (0.03ms, 10.4MB)
# 테스트 4 〉	통과 (0.03ms, 10.3MB)
# 테스트 5 〉	통과 (0.06ms, 10.4MB)
# 테스트 6 〉	통과 (0.04ms, 10.4MB)
# 테스트 7 〉	통과 (0.04ms, 10.4MB)
# 테스트 8 〉	통과 (0.04ms, 10.4MB)
# 테스트 9 〉	통과 (0.05ms, 10.4MB)
# 테스트 10 〉	통과 (0.04ms, 10.5MB)
# 테스트 11 〉	통과 (0.05ms, 10.4MB)
# 테스트 12 〉	통과 (0.05ms, 10.4MB)
# 테스트 13 〉	통과 (0.04ms, 10.5MB)
# 테스트 14 〉	통과 (0.03ms, 10.4MB)
# 테스트 15 〉	통과 (0.03ms, 10.4MB)
# 테스트 16 〉	통과 (0.03ms, 10.4MB)