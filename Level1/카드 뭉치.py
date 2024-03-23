# https://school.programmers.co.kr/learn/courses/30/lessons/159994

def solution(cards1, cards2, goal):
    one, two = 0, 0
    point = 0
    while one < len(cards1) and two < len(cards2):
        if cards1[one] == goal[point]:
            one += 1
            point += 1
        elif cards2[two] == goal[point]:
            two += 1
            point += 1
        else:
            return "No"
        
        if point == len(goal):
            return 'Yes'
        
    if one < len(cards1):
        return "Yes" if cards1[one:] == goal[point:] else "No"
    else:
        return "Yes" if cards2[two:] == goal[point:] else "No"


print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
# "YES"
print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
# "NO"


# 테스트 1 〉	통과 (0.00ms, 10.3MB)
# 테스트 2 〉	통과 (0.00ms, 10.2MB)
# 테스트 3 〉	통과 (0.00ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.4MB)
# 테스트 5 〉	통과 (0.00ms, 10.2MB)
# 테스트 6 〉	통과 (0.00ms, 10.3MB)
# 테스트 7 〉	통과 (0.01ms, 10.4MB)
# 테스트 8 〉	통과 (0.00ms, 10.3MB)
# 테스트 9 〉	통과 (0.00ms, 10.2MB)
# 테스트 10 〉	통과 (0.01ms, 10.4MB)
# 테스트 11 〉	통과 (0.01ms, 10.3MB)
# 테스트 12 〉	통과 (0.01ms, 10.4MB)
# 테스트 13 〉	통과 (0.01ms, 10.2MB)
# 테스트 14 〉	통과 (0.01ms, 10.2MB)
# 테스트 15 〉	통과 (0.01ms, 10.3MB)
# 테스트 16 〉	통과 (0.02ms, 10.2MB)
# 테스트 17 〉	통과 (0.01ms, 10.2MB)
# 테스트 18 〉	통과 (0.02ms, 10.4MB)
# 테스트 19 〉	통과 (0.01ms, 10.2MB)
# 테스트 20 〉	통과 (0.01ms, 10.3MB)
# 테스트 21 〉	통과 (0.01ms, 10.4MB)
# 테스트 22 〉	통과 (0.01ms, 10.2MB)
# 테스트 23 〉	통과 (0.01ms, 10.2MB)
# 테스트 24 〉	통과 (0.00ms, 10.3MB)
# 테스트 25 〉	통과 (0.01ms, 10.2MB)