# https://school.programmers.co.kr/learn/courses/30/lessons/142086

from collections import defaultdict

def solution(s):
    s = 'a' + s
    dictionary = defaultdict(int)
    answer = []
    for n, alpha in enumerate(s):
        if dictionary[alpha] == 0:
            answer.append(-1)
        else:
            answer.append(n - dictionary[alpha])
            
        dictionary[alpha] = n
    return answer[1:]

print(solution('banana'))
# [-1, -1, -1, 2, 2, 2]
print(solution('foobar'))
# [-1, -1, 1, -1, -1, -1]

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.03ms, 10.3MB)
# 테스트 3 〉	통과 (0.03ms, 10.2MB)
# 테스트 4 〉	통과 (0.17ms, 10.2MB)
# 테스트 5 〉	통과 (3.36ms, 11.1MB)
# 테스트 6 〉	통과 (0.69ms, 10.3MB)
# 테스트 7 〉	통과 (1.72ms, 11.2MB)
# 테스트 8 〉	통과 (0.60ms, 10.4MB)
# 테스트 9 〉	통과 (1.73ms, 11MB)
# 테스트 10 〉	통과 (0.55ms, 10.3MB)
# 테스트 11 〉	통과 (1.56ms, 10.9MB)
# 테스트 12 〉	통과 (0.01ms, 10.2MB)
# 테스트 13 〉	통과 (0.01ms, 10.3MB)
# 테스트 14 〉	통과 (0.09ms, 10.3MB)
# 테스트 15 〉	통과 (0.01ms, 10.2MB)
# 테스트 16 〉	통과 (0.02ms, 10.2MB)
# 테스트 17 〉	통과 (0.02ms, 10.1MB)
# 테스트 18 〉	통과 (0.32ms, 10.3MB)
# 테스트 19 〉	통과 (0.37ms, 10.3MB)
# 테스트 20 〉	통과 (0.15ms, 10.3MB)
# 테스트 21 〉	통과 (0.02ms, 10.2MB)
# 테스트 22 〉	통과 (0.77ms, 10.3MB)
# 테스트 23 〉	통과 (0.08ms, 10.3MB)
# 테스트 24 〉	통과 (0.11ms, 10.3MB)
# 테스트 25 〉	통과 (0.13ms, 10.2MB)
# 테스트 26 〉	통과 (0.03ms, 10.2MB)
# 테스트 27 〉	통과 (0.13ms, 10.3MB)
# 테스트 28 〉	통과 (0.12ms, 10.3MB)
# 테스트 29 〉	통과 (0.01ms, 10.2MB)
# 테스트 30 〉	통과 (1.76ms, 11.2MB)