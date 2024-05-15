# https://school.programmers.co.kr/learn/courses/30/lessons/92341

from collections import defaultdict
import math

def solution(fees, records):
    last_time = 23*60+59
    dictionary = defaultdict(int)
    in_parking = {}
    for record in records:
        time, number, act = record.split()
        hour, minu = time.split(':')
        cur_time = int(hour) * 60 + int(minu)
        if act == 'IN':
            in_parking[number] = cur_time
        else:
            dictionary[number] += cur_time - in_parking[number]
            del in_parking[number]
    
    for number in in_parking.keys():
        dictionary[number] += last_time - in_parking[number]
    total_fees = sorted(dictionary.items(), key=lambda x:x[0])
    
    answer = []
    for car_num, times in total_fees:
        if times <= fees[0]:
            answer.append(fees[1])
        else:
            price = fees[1] + math.ceil((times - fees[0]) / fees[2]) * fees[3]
            answer.append(price)
    
    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
# [14600, 34400, 5000]
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
# [0, 591]
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
# [14841]

# 테스트 1 〉	통과 (0.05ms, 10.4MB)
# 테스트 2 〉	통과 (0.03ms, 10.4MB)
# 테스트 3 〉	통과 (0.04ms, 10.2MB)
# 테스트 4 〉	통과 (0.07ms, 10.3MB)
# 테스트 5 〉	통과 (0.15ms, 10.3MB)
# 테스트 6 〉	통과 (0.18ms, 10.4MB)
# 테스트 7 〉	통과 (1.43ms, 10.4MB)
# 테스트 8 〉	통과 (0.81ms, 10.3MB)
# 테스트 9 〉	통과 (0.17ms, 10.3MB)
# 테스트 10 〉	통과 (1.14ms, 10.3MB)
# 테스트 11 〉	통과 (1.53ms, 10.5MB)
# 테스트 12 〉	통과 (1.76ms, 10.6MB)
# 테스트 13 〉	통과 (0.03ms, 10.3MB)
# 테스트 14 〉	통과 (0.03ms, 10.4MB)
# 테스트 15 〉	통과 (0.03ms, 10.4MB)
# 테스트 16 〉	통과 (0.03ms, 10.3MB)