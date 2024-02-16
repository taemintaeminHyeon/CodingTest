'''
1~number까지의 숫자를 약수의 개수를 구한 후
모든 숫자에 해당하는 약수의 개수를 더한다.
만약 약수의 개수가 limit을 넘는경우 power 값으로 변경하여
약수의 개수를 더한다.


'''

def solution(number, limit, power):
    answer = 0

    for i in range(1, number+1):
        count = 0

        for j in range(1, int(i**(1/2)) + 1):
            if i % j == 0:
                count += 1
                if ((j**2) != i):
                    count += 1

        if count > limit:
            answer += power
        else:
            answer += count

    return answer
