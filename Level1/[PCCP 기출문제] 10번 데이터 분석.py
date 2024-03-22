# https://school.programmers.co.kr/learn/courses/30/lessons/250121

def solution(data, ext, val_ext, sort_by):
    # code, date, maximum, remain
    dictionary = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    
    answer = []
    
    for d in data:
        if d[dictionary[ext]] < val_ext:
            answer.append(d)
    answer = sorted(answer, key=lambda x: x[dictionary[sort_by]])
    return answer

print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date", 20300501, "remain"))
# [[3,20300401,10,8],[1,20300104,100,80]]