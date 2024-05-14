# https://school.programmers.co.kr/learn/courses/30/lessons/250135

def calc(h, m, s):
    cnt = -1

    h_angle, m_angle, s_angle = (h*30 + m*0.5 + s*0.5/60) % 360, m*6+s*0.1, s*6
    if s_angle >= h_angle:
        cnt += 1
    if s_angle >= m_angle:
        cnt += 1
    
    cnt += (h*60+m) * 2 - h
    
    if h >= 12:
        cnt -= 2
        
    return cnt
    
def solution(h1, m1, s1, h2, m2, s2):
    c1 = calc(h1, m1, s1)
    c2 = calc(h2, m2, s2)
    print(c1, c2)
    # if (h1 == 0 or h1 == 12) and m1 == 0 and s1 == 0:
    #     c2 += 1
    
    return c2 - c1

# print(solution(0, 5, 30, 0, 7, 0))
# # 2
# print(solution(12, 0, 0, 12, 0, 30))
# # 1
# print(solution(0, 6, 1, 0, 6, 6))
# # 0
# print(solution(11, 59, 30, 12, 0, 0))
# # 1
# print(solution(11, 58, 59, 11, 59, 0))
# # 1
# print(solution(1, 5, 5, 1, 5, 6))
# # 2
# print(solution(0, 0, 0, 23, 59, 59))
# # 2852


print(solution(0, 0, 0, 12, 0, 0))
