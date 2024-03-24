# https://school.programmers.co.kr/learn/courses/30/lessons/118666

from collections import defaultdict

def compare(dictionary):
    answer = ''
    answer += 'R' if dictionary['R'] >= dictionary['T'] else 'T'
    answer += 'C' if dictionary['C'] >= dictionary['F'] else 'F'
    answer += 'J' if dictionary['J'] >= dictionary['M'] else 'M'
    answer += 'A' if dictionary['A'] >= dictionary['N'] else 'N'
    return answer
        

def solution(survey, choices):
    # RT, CF, JM, AN
    scores = [3, 2, 1, 0, 1, 2, 3]
    
    dictionary = defaultdict(int)
    for sur, cho in zip(survey, choices):
        cho = cho-1
        if cho < 3:
            dictionary[sur[0]] += scores[cho]
        elif cho == 3:
            continue
        else:
            dictionary[sur[1]] += scores[cho]
            
    return compare(dictionary)

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
# TCMA
print(solution(["TR", "RT", "TR"], [7, 1, 3]))
# RCJA


# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.02ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.3MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.02ms, 10.2MB)
# 테스트 8 〉	통과 (0.02ms, 10.2MB)
# 테스트 9 〉	통과 (0.02ms, 10.2MB)
# 테스트 10 〉	통과 (0.04ms, 10.3MB)
# 테스트 11 〉	통과 (0.02ms, 10.4MB)
# 테스트 12 〉	통과 (0.09ms, 10.2MB)
# 테스트 13 〉	통과 (0.08ms, 10.2MB)
# 테스트 14 〉	통과 (0.12ms, 10.4MB)
# 테스트 15 〉	통과 (0.13ms, 10.3MB)
# 테스트 16 〉	통과 (0.15ms, 10.2MB)
# 테스트 17 〉	통과 (0.15ms, 10.4MB)
# 테스트 18 〉	통과 (0.14ms, 10.2MB)
# 테스트 19 〉	통과 (0.27ms, 10.2MB)
# 테스트 20 〉	통과 (0.15ms, 10.2MB)