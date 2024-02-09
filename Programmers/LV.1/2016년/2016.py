def solution(a, b):
    answer = ''
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    monthDays=[31,29,31,30,31,30,31,31,30,31,30,31]
    totalDay = 0
    for i in range(a-1):
        totalDay += monthDays[i]

    totalDay += b

    answer = day[totalDay % 7]

    return answer

print(solution(5, 24))