'''
생각 흐름

인물과 점수가 매핑이 되므로
파이썬의 딕셔너리를 사용하면 쉽게 값을 찾아올 수 있을 거라 생각

이후 제시되는 배열의 이름을 저장해둔 딕셔너리와 비교해서
값이 있으면 점수를 반환하고 없으면 0을 반환하여
중간 계산에 저장한 뒤
최종 배열을 출력한다.


'''


def solution(name, yearning, photo):

    point = dict(zip(name, yearning))
    answer = []

    for i in photo :
        checkSum = 0
        for j in i :
            if j in point :
                checkSum += point[j]
            else:
                checkSum += 0

        answer.append(checkSum)

    return answer