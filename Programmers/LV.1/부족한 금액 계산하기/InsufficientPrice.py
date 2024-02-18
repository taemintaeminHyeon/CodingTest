'''
반복문을 통해 count 수 만큼 계산된 값을 money에서 차감하고
최종 값이 마이너스면 절대값을 아니라면 0을 반환한다.
'''

def solution(price, money, count):
    answer = money

    for i in range(1, count+1):
        answer -= price * i

    if answer < 0:
        answer = abs(answer)
    else:
        answer = 0

    return answer


print(solution(3, 20, 4))