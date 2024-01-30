'''
생각 흐름

최대 공약수는 두 수를 나눌 수 있는 최대 수를 구하는 것이므로
두 수 중 작은 수부터 1까지 나눠 두 수를 모두 나눠 떨어지게 하는 수를 구한다.

최소 공배수는 반대로 두 수의 공통 배수를 구해야하므로
두 수중 큰 수를 기준으로 두 수의 곱한 수 까지의 수에
입력받은 수를 나눠 공통 배수를 구한다.

'''

def solution(n, m):
    answer = []

    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break

    for i in range(max(n, m), (n*m)+1):
        if i % n == 0 and i % m == 0:
            answer.append(i)
            break

    return answer

print(solution(2,4))
