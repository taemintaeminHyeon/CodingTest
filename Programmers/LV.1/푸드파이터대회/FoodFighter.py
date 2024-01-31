'''
문제를 분석하면
결국 0을 기준으로 반전된 문자열이 존재할 수 밖에 없기 떄문에
받은 리스트에서 첫번째의 1은 물인 0을 의미하고
나머지에서 1이 나오면 사용될 수 없기 떄문에

아래의 반복문을 작성해 1인 경우 사용될 일이 없도록 하고
나머지 부분은 갯수를 반으로 나눠 몫만큼 인덱스의 번호(음식 번호)를 추가한다
그 후 0을 추가한 후
해당 문자열을 역으로 바꿔
문자열0역문자열을 반환한다.
'''

def solution(food):
    answer = ''

    for index, num in enumerate(food):
        for j in range(int(num/2)):
            answer += str(index)

    reverse = answer[::-1]

    answer = answer + '0' + reverse


    return answer


print(solution([1,3,4,6]))