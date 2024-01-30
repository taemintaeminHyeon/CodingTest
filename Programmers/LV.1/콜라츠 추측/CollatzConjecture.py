'''
입력된 수를 먼저 1인지 확인 후
이후에 콜라츠 로직을 실행한다.
각 경우에 대해서 로직을 실행하면 횟수를 증가시키고
이후 횟수가 500이상이면 -1을 반환한다.

'''

def solution(num):
    checkNum = num
    answer = 0
    while True:
        if (checkNum == 1):
            break;

        if checkNum % 2 == 0:
            checkNum = checkNum / 2
            answer = answer + 1
        else:
            checkNum = checkNum * 3 + 1
            answer = answer + 1

        if (answer > 499):
            answer = -1
            break;

    return answer