# https://school.programmers.co.kr/learn/courses/30/lessons/136798

def calc(num, limit, power):
    result = {1, num}
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            result.add(i)
            result.add(num // i)
    return len(result) if len(result) <= limit else power

def solution(number, limit, power):
    answer = [1]
    for i in range(2, number+1):
        answer.append(calc(i, limit, power))
    return sum(answer)


print(solution(5, 3, 2))
# 10
print(solution(10, 3, 2))
# 21


# 테스트 1 〉	통과 (38.84ms, 10.2MB)
# 테스트 2 〉	통과 (6.01ms, 10.3MB)
# 테스트 3 〉	통과 (2.50ms, 10.3MB)
# 테스트 4 〉	통과 (7.80ms, 10.2MB)
# 테스트 5 〉	통과 (1.90ms, 10.2MB)
# 테스트 6 〉	통과 (55.93ms, 10.3MB)
# 테스트 7 〉	통과 (6.26ms, 10.2MB)
# 테스트 8 〉	통과 (4.00ms, 10.1MB)
# 테스트 9 〉	통과 (35.15ms, 10.2MB)
# 테스트 10 〉	통과 (2.72ms, 10.2MB)
# 테스트 11 〉	통과 (805.42ms, 10.3MB)
# 테스트 12 〉	통과 (852.01ms, 10.5MB)
# 테스트 13 〉	통과 (795.14ms, 10.5MB)
# 테스트 14 〉	통과 (821.58ms, 10.3MB)
# 테스트 15 〉	통과 (858.10ms, 10.2MB)
# 테스트 16 〉	통과 (892.19ms, 10.2MB)
# 테스트 17 〉	통과 (0.01ms, 10.2MB)
# 테스트 18 〉	통과 (953.84ms, 10.4MB)
# 테스트 19 〉	통과 (5.85ms, 10.2MB)
# 테스트 20 〉	통과 (5.84ms, 10.2MB)
# 테스트 21 〉	통과 (0.01ms, 10.2MB)
# 테스트 22 〉	통과 (0.02ms, 10.2MB)
# 테스트 23 〉	통과 (0.02ms, 10.2MB)
# 테스트 24 〉	통과 (909.14ms, 10.3MB)
# 테스트 25 〉	통과 (898.13ms, 10.2MB)
# 테스트 26 〉	통과 (1.64ms, 10.2MB)
# 테스트 27 〉	통과 (1.81ms, 10.3MB)