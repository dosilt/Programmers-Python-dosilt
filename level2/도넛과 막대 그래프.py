# https://school.programmers.co.kr/learn/courses/30/lessons/258711

from collections import defaultdict

def check(cur_node, dictionary):
    temp = cur_node
    cnt = 0
    while True:
        if len(dictionary[temp]) == 0:
            return 1
        elif len(dictionary[temp]) == 2:
            return 2
        elif temp == cur_node and cnt > 0:
            return 0
        
        cnt += 1
        temp = dictionary[temp][0]
        
        
def solution(edges):
    dictionary = defaultdict(list)
    cases = [0, 0, 0]
    st_node, en_node = set(), set()
    
    for a, b in edges:
        dictionary[a].append(b)
        st_node.add(a)
        en_node.add(b)
    
    candidates = st_node - en_node
    
    center_node = [0, 0]
    for candidate in candidates:
        if len(dictionary[candidate]) > center_node[1]:
            center_node = [candidate, len(dictionary[candidate])]
            
    center_node = center_node[0]
    
    for key in dictionary[center_node]:
        cases[check(key, dictionary)] += 1
    
    answer = [center_node] + cases
    return answer


print(solution([[2, 3], [4, 3], [1, 1], [2, 1]]))
# [2, 1, 1, 0]
print(solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]))
# [4, 0, 1, 2]

# 테스트 1 〉	통과 (0.08ms, 10.3MB)
# 테스트 2 〉	통과 (0.21ms, 10.2MB)
# 테스트 3 〉	통과 (0.18ms, 10.4MB)
# 테스트 4 〉	통과 (0.07ms, 10.3MB)
# 테스트 5 〉	통과 (0.34ms, 10.5MB)
# 테스트 6 〉	통과 (0.37ms, 10.6MB)
# 테스트 7 〉	통과 (0.37ms, 10.3MB)
# 테스트 8 〉	통과 (415.08ms, 116MB)
# 테스트 9 〉	통과 (288.04ms, 83.6MB)
# 테스트 10 〉	통과 (912.67ms, 166MB)
# 테스트 11 〉	통과 (651.79ms, 117MB)
# 테스트 12 〉	통과 (426.75ms, 118MB)
# 테스트 13 〉	통과 (443.98ms, 108MB)
# 테스트 14 〉	통과 (1067.48ms, 212MB)
# 테스트 15 〉	통과 (509.06ms, 108MB)
# 테스트 16 〉	통과 (254.29ms, 88.8MB)
# 테스트 17 〉	통과 (891.56ms, 164MB)
# 테스트 18 〉	통과 (624.47ms, 108MB)
# 테스트 19 〉	통과 (408.48ms, 108MB)
# 테스트 20 〉	통과 (332.25ms, 101MB)
# 테스트 21 〉	통과 (1010.42ms, 201MB)
# 테스트 22 〉	통과 (831.06ms, 184MB)
# 테스트 23 〉	통과 (673.72ms, 183MB)
# 테스트 24 〉	통과 (760.75ms, 184MB)
# 테스트 25 〉	통과 (665.02ms, 184MB)
# 테스트 26 〉	통과 (797.35ms, 184MB)
# 테스트 27 〉	통과 (0.01ms, 10.4MB)
# 테스트 28 〉	통과 (0.01ms, 10.3MB)
# 테스트 29 〉	통과 (0.01ms, 10.2MB)
# 테스트 30 〉	통과 (0.01ms, 10.2MB)
# 테스트 31 〉	통과 (0.01ms, 10.4MB)
# 테스트 32 〉	통과 (0.01ms, 10.2MB)
# 테스트 33 〉	통과 (0.02ms, 10.4MB)
# 테스트 34 〉	통과 (0.01ms, 10.2MB)
# 테스트 35 〉	통과 (0.01ms, 10.3MB)