'''
자연수 n이 하나 이상의
연속된 자연수의 합으로 표현할 수 있는 방법의 수를 구하는 문제
즉 x = n + n+1 + n+2 + ... + k-1 + k 을 구한다.
1 ~ k 까지의 합은 k(k+1)/2
여기서 n~k 까지의 합이므로,
1 ~ n-1 까지의 합을 뺀다.
1~ n-1의 합은 (n-1)n/2
x = k(k+1) / 2 - n(n-1) /2
2x = k^2 + k - n^2 - n

'''

def solution1(n):
    answer = 0

    for i in range(1, n):
        for j in range(1, n):
            if (j*(j+1)/2 - i*(i-1)/2) == n:
                answer += 1


    return answer + 1



'''
위에 방식으로 해보니 시간복잡도가 너무 커진다
그래서 그냥 1~n 까지 더하면서
중간에 n 값이 나오거나(그럼 횟수를 더함) n값을 초과하면(pass)
2~n 까지 해서 n까지 반복하는 걸로 함
'''
def solution2(n):
    answer = 0

    for i in range(1, n + 1):
        sum = 0
        for j in range(i, n + 1):
            sum += j
            if sum == n:
                answer += 1
                break
            elif sum > n:
                break
    return answer


print(solution2(15))