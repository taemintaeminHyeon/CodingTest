'''

생각 흐름

3진법으로 표현해야 하니
기존의 2진법 구하는 방법을 이용해
3진법으로 변환한다

이후 문제에서 나온 수를 뒤짚어서 계산하라고 하였으나
차례대로 계산하면 역으로 뒤집은 수를 자릿수에 맞게 계산한 거와
동일하므로 그냥 계산하여 해결함
'''


def solution(n):
    ternarys = []  # 3진수 저장 리스트
    answer = 0

    while True:

        if n < 3:  # 3보다 작을 경우 3진수 변환할 필요 없음
            ternarys.append(n)
            break

        quotient = int(n / 3)
        remainder = int(n % 3)
        ternarys.insert(0, remainder)  # 계산한 나머지를 리스트의 맨 앞에(insert) 추가
        if quotient < 3:  # 마지막 계산
            ternarys.insert(0, quotient)
            break

        n = quotient

    # enumerate -> 값과 해당 값의 인덱스를 같이 반환할 수 있다.
    for i, ternary in enumerate(ternarys):  # 3진수 -> 10진수 변환
        answer += ternary * (3 ** i)

    return answer


