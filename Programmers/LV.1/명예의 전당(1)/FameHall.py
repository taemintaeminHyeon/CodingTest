'''
k까지는 들어간 값만 비교하면 되며
그 이후부터는 checkScore를 이용해
해당 값과 저장해둔 값을 비교한 후
만약 해당 값이 크면 checkScore에
작은값과 해당 값을 변경한다.
이후
checkScore를 오름차순으로 정렬 하여 맨 처음 있는(제일 작은값)
answer에 추가해 준다.

'''

def solution(k, score):
    answer = []
    checkScore = []

    for i in range(len(score)):
        if len(answer) < k:
            checkScore = sorted(score[:i+1])
            answer.append(checkScore[0])
            continue

        for j in range(k):
            if score[i] > checkScore[j]:
                checkScore[j] = score[i]
                break

        checkScore = sorted(checkScore)
        answer.append(checkScore[0])

    return answer
