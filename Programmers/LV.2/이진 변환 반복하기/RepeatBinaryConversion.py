'''
처음 문자열의 길이를 저장한 후
0을 제외한 문자열의 길이를 통해
0의 수를 구한 후
0의 제외한 문자열의 길이를 2진수로 변환하여
해당 로직을 반복하다 문자열의 길이가 1이될 때
전체 반복횟수와 0의 수를 구한다.
'''

def solution(s):
    answer = []
    count = 0
    repeat = 0
    while True:

        if len(s) == 1:
            break

        firstLength = len(s)
        s = s.replace("0", "")
        secondLength = len(s)

        count += firstLength - secondLength
        s = bin(secondLength)[2:]
        repeat += 1


    answer.append(repeat)
    answer.append(count)
    return answer


