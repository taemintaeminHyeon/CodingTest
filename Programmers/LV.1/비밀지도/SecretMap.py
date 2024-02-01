'''

파이썬 bin 함수를 사용하여 각 두 수의 이진수를 구한다.

여기서 n만큼의 출력을 얻어야 하므로
자리가 모자란다면 0을 추가해 줘야한다.

이때
결과의 앞부분에 이진수를 표현하는 0b가 포함되므로
0b를 제외한 길이가 n보다 작으면 길이가 모자란 것이므로
그 만큼 0을 추가해준다.

이후 앞부분을 제외하고 1은 #으로 0은 " "으로 치환하여
answer에 대입하여 리턴한다.

주의!
반복문 변수 신경쓰자 중복되면 안됨 의미있는 값으로 바꾸도록 하자!
'''

def solution(n, arr1, arr2):
    answer = []
    secretArr= []

    for i in range(n):
        binaryCheck = bin(arr1[i] | arr2[i])
        if len(binaryCheck)-2 < n:
            for j in range(n - (len(binaryCheck)-2)):
                binaryCheck = binaryCheck[:2] + '0' + binaryCheck[2:]

        secretArr.append(binaryCheck)
        secretArr[i] = secretArr[i][2:]
        secretArr[i] = secretArr[i].replace('1', '#')
        secretArr[i] = secretArr[i].replace('0', ' ')
        answer.append(secretArr[i])

    return answer


print(solution(6, [46,33,33,22,31,50], [27,56,19,14,14,10]))