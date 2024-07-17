# https://school.programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    people = sorted(people)
    answer = 0

    left, right = 0, len(people)-1
    
    while left <= right:
        check = True
        cur_weight = people[right]
        right -= 1
        
        if cur_weight + people[right] <= limit:
            cur_weight += people[right]
            right -= 1
            check = False
            
        if cur_weight + people[left] <= limit and check:
            cur_weight += people[left]
            left += 1
        
        cur_weight = 0
        answer += 1
    
    return answer

print(solution([70, 50, 80, 50], 100))
# 3
print(solution([70, 80, 50], 100))
# 3

# 정확성  테스트
# 테스트 1 〉	통과 (2.08ms, 10.3MB)
# 테스트 2 〉	통과 (0.90ms, 10.2MB)
# 테스트 3 〉	통과 (0.85ms, 10.4MB)
# 테스트 4 〉	통과 (0.89ms, 10.3MB)
# 테스트 5 〉	통과 (0.73ms, 10.2MB)
# 테스트 6 〉	통과 (0.28ms, 10.2MB)
# 테스트 7 〉	통과 (0.39ms, 10.3MB)
# 테스트 8 〉	통과 (0.07ms, 10.1MB)
# 테스트 9 〉	통과 (0.10ms, 10.2MB)
# 테스트 10 〉	통과 (0.76ms, 10.2MB)
# 테스트 11 〉	통과 (1.03ms, 10.2MB)
# 테스트 12 〉	통과 (0.79ms, 10.2MB)
# 테스트 13 〉	통과 (0.89ms, 10.2MB)
# 테스트 14 〉	통과 (1.02ms, 10.2MB)
# 테스트 15 〉	통과 (0.16ms, 10.2MB)
# 테스트 16 〉	통과 (0.02ms, 10MB)
# 테스트 17 〉	통과 (0.03ms, 10.2MB)
# 테스트 18 〉	통과 (0.02ms, 10.2MB)
# 테스트 19 〉	통과 (0.03ms, 10.2MB)
# 테스트 20 〉	통과 (0.03ms, 10.3MB)
# 테스트 21 〉	통과 (0.03ms, 10.2MB)
# 테스트 22 〉	통과 (0.02ms, 10.3MB)
# 효율성  테스트
# 테스트 1 〉	통과 (10.89ms, 10.9MB)
# 테스트 2 〉	통과 (12.24ms, 10.9MB)
# 테스트 3 〉	통과 (10.16ms, 10.8MB)
# 테스트 4 〉	통과 (11.78ms, 10.8MB)
# 테스트 5 〉	통과 (10.28ms, 10.8MB)