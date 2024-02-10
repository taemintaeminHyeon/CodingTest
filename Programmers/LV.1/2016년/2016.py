'''
2016년 1월 1일이 금요일이기 때문에
일을 7로 나눈 나머지가 1일 떄가 금요일이다
그러므로 배열 1번을 금요일로 설정하고 나머지를 맞춰 저장한다

이후 각 월 마다 날짜를 더해주고

7을 나눠 요일을 구한다.
'''

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