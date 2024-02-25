'''
주어진 수를 10으로 나누어 각 몫과 나머지를 구해
문제를 해결한다.
'''
def solution(x):
    checkNum = x
    numberList = []
    total = 0
    while True:
        if checkNum // 10 < 1:
            total += checkNum
            break
        total += checkNum % 10
        checkNum = checkNum // 10

    if x % total == 0:
        answer = True
    else:
        answer = False

    return answer

