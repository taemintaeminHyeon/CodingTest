'''

여기서 전에 보았던 조합을 사용하면 되지만
그냥 알고리즘으로 구현해서 풀기로 하였다.

모든 원소에서 2개씩 뽑아 더한 합을 리스트에 저장하고
이때 중복이면 저장하지 않는다.

연습을 위해 조합은 solution2로 구현함
'''


def solution(numbers):
    answer = []
    checkPoint = 0
    for number in numbers:


        for index in range(checkPoint + 1, len(numbers)):
            sum = number + numbers[index]
            if sum not in answer:
                answer.append(sum)
        checkPoint += 1


    answer.sort()
    return answer


def solution2(numbers):
    from itertools import combinations

    answer = []

    combis = list(combinations(numbers,2))
    for combi in combis:
        sum = combi[0] + combi[1]
        if sum not in answer:
            answer.append(sum)

    answer.sort()

    return answer



