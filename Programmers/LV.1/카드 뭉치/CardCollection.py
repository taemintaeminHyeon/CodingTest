'''

처음에는 모든 조합을 이용해 문자를 비교하려고 하였지만
그렇게 하면 시간복잡도가 n**3이 나오기 때문에
포기하고 다른 방식을 생각함

사실 목표하는 문자열과 동일한지만 확인하면 되는거기 때문에
먼저 첫번째 카드의 단어와 목표 문자열의 단어를 비교한다.
이때 해당하지 않으면
두번째 카드에 속하는 것이기 때문에
두번째 카드의 단어와 목표 문자열을 비교
이때도 동일하지 않으면
만들 수 없는 문장이기 때문에
No를 반환한다.

그리고 여기서 카드를 다 써버리는 경우도 존재하기 때문에
카드가 존재하는 경우 비교하도록 조건을 추가해준다. -> 카드의 단어가 존재하지 않으면 비교할 수도 필요도 없음
'''

def solution(cards1, cards2, goal):
    answer = 'Yes'
    for target in goal:
        if cards1 and target == cards1[0]:
            cards1.pop(0)
        elif cards2 and target == cards2[0]:
            cards2.pop(0)
        else:
            answer = "No"

    return answer


