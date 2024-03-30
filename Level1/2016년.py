# https://school.programmers.co.kr/learn/courses/30/lessons/12901


def solution(a, b):
    days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    total_days = (sum(months[:a-1]) + b + 4) % 7
    return days[total_days]

print(solution(5, 24))
# 'TUE

# 테스트 1 〉	통과 (0.00ms, 10.2MB)
# 테스트 2 〉	통과 (0.00ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.00ms, 10MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.00ms, 10MB)
# 테스트 7 〉	통과 (0.01ms, 9.93MB)
# 테스트 8 〉	통과 (0.00ms, 10.3MB)
# 테스트 9 〉	통과 (0.01ms, 10.3MB)
# 테스트 10 〉	통과 (0.00ms, 10.2MB)
# 테스트 11 〉	통과 (0.00ms, 10.1MB)
# 테스트 12 〉	통과 (0.00ms, 10.1MB)
# 테스트 13 〉	통과 (0.00ms, 10.3MB)
# 테스트 14 〉	통과 (0.00ms, 10.3MB)