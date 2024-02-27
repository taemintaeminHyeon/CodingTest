'''
제공 받은 두 정수 중 작은 값을 찾아
해당 수 부터 다른 수 까지 반복문을 사용하여 값을 더한다.
'''

def solution(a,b):
    answer = 0

    if a > b:
        for i in range(b, a+1):
            answer += i
    else:
        for i in range(a, b+1):
            answer += i


    return answer

