'''
먼저 플레이어의 수를 가져온다
그 후 해당 스테이지에 속한 플레이어를 전체 플레이어 수로 나누어 실패율을 구한 후
해당 단계는 계산하였기 때문에 해당 스테이지에 머무른 플레이어는 제외한다.
만약 플레이어가 없다면 모두 실패한것이므로 0을 딕셔너리에 저장
이후 실패율을 기준으로 정렬하여 해당 key값을 리스트로 반환한다.
'''

def solution(N, stages):
    dictionary = {}
    players = len(stages)

    for i in range(1, N+1):
        count = stages.count(i)
        if players == 0:
            dictionary[i] = 0
        else:
            dictionary[i] = count / players

        players -= count

    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

    return list(sorted_dict.keys())

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))