'''
생각 흐름

요구한 금액을 오름차수로 정렬하고
적은 예산의 부서부터 예산을 배정한다면
최대 수의 부서에 배정할 수 있다.
'''

def solution(d, budget):
    answer = 0

    d.sort()

    for i in d:
        budget -= i
        if budget < 0:
            break;
        else:
            answer += 1


    return answer
