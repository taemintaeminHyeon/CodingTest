'''
각 리스트에 값을 가져와
True면 양수이므로 더하고
False이면 음수이므로 빼서
총 합을 구한다.
'''


def solution(absolutes, signs):
    answer = 0

    for i, j in zip(absolutes, signs):
        if j:
            answer += i
        else:
            answer -= i

    return answer
