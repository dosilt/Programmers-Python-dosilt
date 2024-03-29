# https://school.programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number):
    answer = '*' * (len(phone_number) - 4) + phone_number[-4:]
    return answer

print(solution("01033334444"))
# *******4444
print(solution("027778888"))
# *****8888

# 테스트 1 〉	통과 (0.00ms, 10.1MB)
# 테스트 2 〉	통과 (0.00ms, 10.2MB)
# 테스트 3 〉	통과 (0.00ms, 10.3MB)
# 테스트 4 〉	통과 (0.00ms, 10.3MB)
# 테스트 5 〉	통과 (0.00ms, 10.2MB)
# 테스트 6 〉	통과 (0.00ms, 10.2MB)
# 테스트 7 〉	통과 (0.00ms, 10.2MB)
# 테스트 8 〉	통과 (0.00ms, 10.1MB)
# 테스트 9 〉	통과 (0.00ms, 10.2MB)
# 테스트 10 〉	통과 (0.00ms, 10.2MB)
# 테스트 11 〉	통과 (0.00ms, 10.2MB)
# 테스트 12 〉	통과 (0.00ms, 10MB)
# 테스트 13 〉	통과 (0.00ms, 10.2MB)