'''
set을 사용해 중복을 제거한다 => 이렇게 하면 다른 종류만 남음 => 만들 수 있는 최대 조합 원소 수
이때 중복의 길이가 주어진 num/2 보다 크면 모든 원소를 사용할 수 없으므로 최대수는 num/2
아니라면 set의 길이를 반환한다.

'''

def solution(nums):
    answer = min(len(set(nums)), len(nums)/2)

    return answer

print(solution([3,3,3,2,2,4]))