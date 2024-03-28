# https://school.programmers.co.kr/learn/courses/30/lessons/17681

def flip(board):
    temp = []
    for b in board:
        temp.append(b[::-1])
    return temp

def create_matrix(n, arr1):
    board = []
    for arr in arr1:
        a = arr
        temp = []
        while a > 0:
            a, b = divmod(a, 2)
            temp.append(b)
        board.append(temp + [0] * (n - len(temp)))
    return board        

def solution(n, arr1, arr2):
    board1 = flip(create_matrix(n, arr1))
    board2 = flip(create_matrix(n, arr2))
    
    answer = []
    for row in range(n):
        temp = ''
        for col in range(n):
            if board1[row][col] or board2[row][col]:
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
# ["#####","# # #", "### #", "# ##", "#####"]
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
# ["######", "### #", "## ##", " #### ", " #####", "### # "]

# 테스트 1 〉	통과 (0.10ms, 10.2MB)
# 테스트 2 〉	통과 (0.15ms, 10.2MB)
# 테스트 3 〉	통과 (0.02ms, 10.2MB)
# 테스트 4 〉	통과 (0.11ms, 10.2MB)
# 테스트 5 〉	통과 (0.04ms, 10.2MB)
# 테스트 6 〉	통과 (0.15ms, 10.2MB)
# 테스트 7 〉	통과 (0.04ms, 10.2MB)
# 테스트 8 〉	통과 (0.04ms, 10.1MB)