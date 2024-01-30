'''
생각 흐름

문자열 t를 p의 길이만큼 나눈 문자열을 구해야 하므로
p의 길이를 구한 후
슬라이싱을 이용하여 문자열을 p의 길이만큼 슬라이싱 해
부분문자열을 구한다

이후 해당 부분문자열을 p의 값과 비교하여
작거나 같은 횟수를 카운트하여 반환한다.
'''

def solution(t, p):
    answer = 0
    length = len(p)
    index = 0

    while True:
        if length+index > len(t):
            break

        if int(t[0+index:length+index]) <= int(p):
            answer += 1
        index += 1



    return answer


print(solution("10203", "15"))