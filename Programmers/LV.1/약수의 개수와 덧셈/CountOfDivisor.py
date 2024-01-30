'''
생각 흐름
주어진 범위 사이의 자연수를 배열에 저장
이후 나머지가 0인 경우를 찾고 count
count값이 짝수면 +
마이너스면 - 하여 결과값 리턴
'''


def solution(left, right):
    answer = 0

    numbers= []
    for i in range(left,right+1):
        numbers.append(i)

    for number in numbers:
        count = 0
        for i in range(1,number+1) :
            if number % i == 0:
                count += 1

        if count % 2 == 0 :
            answer += number
        else:
            answer -= number


    return answer
