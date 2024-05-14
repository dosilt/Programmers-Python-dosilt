# https://school.programmers.co.kr/learn/courses/30/lessons/131701

def solution(elements):
    length = len(elements)
    elements = elements + elements[:-1]
    
    candidates = set()
    for i in range(length):
        for j in range(i, length+i-1):
            candidates.add(sum(elements[i:j+1]))
            
    return len(candidates) + 1

print(solution([7, 9, 1, 1, 4]))
# 18

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (51.38ms, 13.1MB)
# 테스트 3 〉	통과 (157.09ms, 13.8MB)
# 테스트 4 〉	통과 (367.96ms, 18.3MB)
# 테스트 5 〉	통과 (722.44ms, 27MB)
# 테스트 6 〉	통과 (1069.72ms, 26.8MB)
# 테스트 7 〉	통과 (1536.57ms, 27MB)
# 테스트 8 〉	통과 (2308.35ms, 27.8MB)
# 테스트 9 〉	통과 (3532.48ms, 43.6MB)
# 테스트 10 〉	통과 (4837.63ms, 43.6MB)
# 테스트 11 〉	통과 (853.06ms, 26.8MB)
# 테스트 12 〉	통과 (1022.74ms, 26.9MB)
# 테스트 13 〉	통과 (1242.45ms, 26.9MB)
# 테스트 14 〉	통과 (1773.11ms, 26.9MB)
# 테스트 15 〉	통과 (2039.38ms, 26.9MB)
# 테스트 16 〉	통과 (3462.46ms, 43.6MB)
# 테스트 17 〉	통과 (3079.78ms, 43.6MB)
# 테스트 18 〉	통과 (3265.77ms, 43.7MB)
# 테스트 19 〉	통과 (3948.33ms, 43.8MB)
# 테스트 20 〉	통과 (4843.04ms, 43.6MB)