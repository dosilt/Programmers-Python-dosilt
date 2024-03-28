# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def match(kind, answers):
    length = len(kind)
    result = 0
    for n, answer in enumerate(answers):
        if answer == kind[n % length]:
            result += 1
    return result
            


def solution(answers):
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score = [0, 0, 0]
    score[0] = match(person1, answers)
    score[1] = match(person2, answers)
    score[2] = match(person3, answers)
    
    answer = []
    max_score = max(score)
    for i in range(3):
        if max_score == score[i]:
            answer.append(i+1)
    
    return answer

print(solution([1, 2, 3, 4, 5]))
# [1]
print(solution([1, 3, 2, 4, 2]))
# [1, 2, 3]



# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.02ms, 10.2MB)
# 테스트 6 〉	통과 (0.04ms, 10.2MB)
# 테스트 7 〉	통과 (1.27ms, 10.1MB)
# 테스트 8 〉	통과 (0.45ms, 10.2MB)
# 테스트 9 〉	통과 (2.46ms, 10.2MB)
# 테스트 10 〉	통과 (2.19ms, 10MB)
# 테스트 11 〉	통과 (4.80ms, 10.2MB)
# 테스트 12 〉	통과 (4.31ms, 10.2MB)
# 테스트 13 〉	통과 (0.13ms, 10.2MB)
# 테스트 14 〉	통과 (2.52ms, 10.3MB)