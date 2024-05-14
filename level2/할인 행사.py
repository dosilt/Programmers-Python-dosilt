# https://school.programmers.co.kr/learn/courses/30/lessons/131127

from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    dictionary = defaultdict(int)
    for key, value in zip(want, number):
        dictionary[key] = value
    for n, item in enumerate(discount):
        dictionary[item] -= 1
        if n >= 9:
            for w in want:
                if dictionary[w] > 0:
                    break
            else:
                answer += 1
            dictionary[discount[n-9]] += 1
            
    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], 
               ["chicken", "apple", "apple", "banana", "rice", 
                "apple", "pork", "banana", "pork", "rice", 
                "pot", "banana", "apple", "banana"]))
# 3
print(solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))
# 0
print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana", "chicken", "apple"]))
# 3
print(solution(["banana", "apple", "rice"], [3, 2, 2], ["apple", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana", "chicken", "apple"]))
# 1

# 테스트 1 〉	통과 (3.67ms, 10.5MB)
# 테스트 2 〉	통과 (26.65ms, 14.7MB)
# 테스트 3 〉	통과 (5.21ms, 11.1MB)
# 테스트 4 〉	통과 (24.39ms, 15.6MB)
# 테스트 5 〉	통과 (14.33ms, 13MB)
# 테스트 6 〉	통과 (2.61ms, 10.4MB)
# 테스트 7 〉	통과 (7.82ms, 11.3MB)
# 테스트 8 〉	통과 (33.17ms, 17.3MB)
# 테스트 9 〉	통과 (5.89ms, 11.1MB)
# 테스트 10 〉	통과 (16.70ms, 13.8MB)
# 테스트 11 〉	통과 (3.73ms, 10.5MB)
# 테스트 12 〉	통과 (0.01ms, 10.2MB)