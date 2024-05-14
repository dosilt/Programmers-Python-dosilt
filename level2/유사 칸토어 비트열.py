# https://school.programmers.co.kr/learn/courses/30/lessons/148652

# 1 -> 11011
# 0 -> 00000


# 1
# 11011
# 11011 11011 00000 11011 11011

def solution(n, l, r):
    answer = 0
    for i in range(l-1,r):
        while i > 0:
            i, mod = divmod(i, 5)
            if mod == 2:
                break
        else:
            answer += 1
    return answer

print(solution(2, 4, 17))
# 8