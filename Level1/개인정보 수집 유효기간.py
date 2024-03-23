# https://school.programmers.co.kr/learn/courses/30/lessons/150370

def selection(cur_day, expire_day):
    for c, e in zip(cur_day, expire_day):
        if c < e:
            return False
        elif c > e:
            return True
    return True

def solution(today, terms, privacies):
    t_year, t_month, t_day = list(map(int, today.split('.')))
    
    dictionary = {}
    for term in terms:
        rule, month = term.split()
        dictionary[rule] = int(month)
        
    answer = []

    for n, private in enumerate(privacies):
        start, rule = private.split()
        s_year, s_month, s_day = list(map(int, start.split('.')))
        
        a, b = divmod(s_month - 1 + dictionary[rule], 12)
        s_year += a
        s_month = b + 1
        
        if selection([t_year, t_month, t_day], [s_year, s_month, s_day]):
            answer.append(n+1)
        
    return answer


print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
# [1, 3]
# print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
# # [1, 4, 5]

# 테스트 1 〉	통과 (0.03ms, 10.2MB)
# 테스트 2 〉	통과 (0.05ms, 10.4MB)
# 테스트 3 〉	통과 (0.05ms, 10.4MB)
# 테스트 4 〉	통과 (0.05ms, 10.4MB)
# 테스트 5 〉	통과 (0.07ms, 10.4MB)
# 테스트 6 〉	통과 (0.08ms, 10.5MB)
# 테스트 7 〉	통과 (0.08ms, 10.4MB)
# 테스트 8 〉	통과 (0.05ms, 10.1MB)
# 테스트 9 〉	통과 (0.17ms, 10.4MB)
# 테스트 10 〉	통과 (0.11ms, 10.3MB)
# 테스트 11 〉	통과 (0.17ms, 10.3MB)
# 테스트 12 〉	통과 (0.20ms, 10.1MB)
# 테스트 13 〉	통과 (0.35ms, 10.4MB)
# 테스트 14 〉	통과 (0.12ms, 10.2MB)
# 테스트 15 〉	통과 (0.12ms, 10.4MB)
# 테스트 16 〉	통과 (0.20ms, 10.4MB)
# 테스트 17 〉	통과 (0.19ms, 10.3MB)
# 테스트 18 〉	통과 (0.18ms, 10.2MB)
# 테스트 19 〉	통과 (0.28ms, 10.4MB)
# 테스트 20 〉	통과 (0.20ms, 10.4MB)