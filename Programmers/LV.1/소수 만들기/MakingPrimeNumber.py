'''
조합을 통해 주어진 리스트 원소 중 3개를 뽑은 경우를 모두 만든다.
이 경우에서의 원소의 합을 구한 후 이것이 2 ~ 원소의 합 -1 까지 수로 나누었을 때 나누어지면 소수가 아니므로 다음 경우로 넘어가고
반복문이 끝까지 가면 소수이므로 answer을 1 카운트 한다.
모두 반복하면 만들 수 있는 소수의 경우의 수가 나온다.
'''
def solution(nums):
    from itertools import combinations

    answer = 0
    combi = list(combinations(nums, 3))
    for i in range(len(combi)):
        check = 0
        for j in range(3):
            check += combi[i][j]

        for k in range(2, check):
            if check % k == 0:
                break
            if k == check - 1:
                answer += 1





    return answer


