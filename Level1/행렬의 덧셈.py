# https://school.programmers.co.kr/learn/courses/30/lessons/12950


def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr1[0]))] for _ in range(len(arr1))]
    for row in range(len(arr1)):
        for col in range(len(arr1[0])):
            answer[row][col] = arr1[row][col] + arr2[row][col]
    return answer

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
# [[4,6],[7,9]]
print(solution([[1],[2]], [[3],[4]]))
# [[4],[6]]


# 테스트 1 〉	통과 (0.01ms, 9.95MB)
# 테스트 2 〉	통과 (0.10ms, 10.1MB)
# 테스트 3 〉	통과 (0.29ms, 10.3MB)
# 테스트 4 〉	통과 (0.17ms, 10.3MB)
# 테스트 5 〉	통과 (0.07ms, 10.1MB)
# 테스트 6 〉	통과 (0.29ms, 10.2MB)
# 테스트 7 〉	통과 (0.02ms, 10.2MB)
# 테스트 8 〉	통과 (0.10ms, 10.2MB)
# 테스트 9 〉	통과 (1.15ms, 10.8MB)
# 테스트 10 〉	통과 (0.86ms, 10.6MB)
# 테스트 11 〉	통과 (0.97ms, 10.4MB)
# 테스트 12 〉	통과 (0.71ms, 10.7MB)
# 테스트 13 〉	통과 (0.53ms, 10.7MB)
# 테스트 14 〉	통과 (0.68ms, 10.5MB)
# 테스트 15 〉	통과 (0.76ms, 10.6MB)
# 테스트 16 〉	통과 (0.74ms, 10.4MB)
# 테스트 17 〉	통과 (45.27ms, 22.8MB)