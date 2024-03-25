'''
칠해야 하는 영역부터 시작한다.
해당 영역 부터 m 만큼 칠하는데
만약 해당 영역이 칠해져 있는 경우는 칠해야 할 이유가 없다.
즉 남은 배열(영역) 부분이 칠해져 있지 않는 경우만 칠하고 카운트한다.
'''


def solution(n, m, section):
    answer = 0
    check = 0
    for num in section:
        if num > check:
            check = num + m - 1
            answer += 1

    return answer
