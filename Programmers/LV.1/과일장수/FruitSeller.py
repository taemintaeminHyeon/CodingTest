'''
m개의 사과를 한 상자에 담을 수 있으므로
score를 m으로 나눠 몇개의 상자에 담을 수 있는지 알아낸다
이후 정렬된 score를 이용해 m개씩 분류 하여
m개 중 가장 낮은 score의 값으로 점수를 계산하여
최종값에 더한다.

'''

def solution(k, m, score):
    answer = 0
    index = 0
    score.sort(reverse=True)
    amountBox = (int)(len(score) / m)

    for i in range(amountBox + 1):

        sortList = []
        for j in range(m):
            if index < len(score):
                sortList.append(score[index])
                index += 1

        if len(sortList) < m:
            answer += 0
            break

        answer += sortList[m-1] * m

    return answer

print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))