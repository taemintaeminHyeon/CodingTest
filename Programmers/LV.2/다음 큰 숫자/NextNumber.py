'''
우선 입력받은 n을 2진수로 변환 후
1의 갯수를 저장한다
이후 n을 1씩 증가하여 2진수로 변환 후
1의 갯수가 같을 때까지 반복하여
같으면 반환한다.
'''

def solution(n):
    answer = n+1
    count = 0


    number = bin(n)[2:]

    for i in number:   # 1의 갯수 카운트
        if i == "1":
            count += 1

    while True:
        checkCount = 0
        check = bin(answer)[2:]
        for i in check:
            if i == "1":
                checkCount += 1

        if checkCount == count:
            break

        answer += 1

    return answer


print(solution(15))