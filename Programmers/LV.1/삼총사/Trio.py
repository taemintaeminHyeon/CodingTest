
'''
생각 흐름

리스트가 1~5까지 있다면
123,124,125 ~ 345

이렇게 모든 리스트를 탐색하여 값을 더한 후
합이 0이면 answer을 카운트한다.

분기점을 추가하기 위해
firstCount, secondCount, thirdCount를 추가하여
다음 반복문의 시작점을 설정해 준다

추가 : 파이썬에서
import itertools
의 combinations를 사용하면 위의 반복문을
사용해 조합을 구해준다
=> 아래의 Combination 함수 참조

'''



def solution(number):
    answer = 0
    firstCount = 0



    for i in number[:-2]:
        check = [i]

        secondCount = firstCount
        thirdCount = firstCount


        for j in number[1+secondCount:-1]:
            check.append(j)

            for k in number[2+thirdCount:]:
                check.append(k)

                sum = check[0] + check[1] + check[2]
                check.pop()
                if sum == 0:
                    answer += 1

            thirdCount += 1
            check.pop()

        secondCount += 1
        firstCount = firstCount + 1


    return answer


def Combination(number):
    from itertools import combinations
    cnt = 0
    for i in combinations(number, 3):
        if sum(i) == 0:
            cnt += 1
    return cnt


