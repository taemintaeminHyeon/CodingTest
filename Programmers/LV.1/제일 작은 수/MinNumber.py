'''
가장 작은수를 찾아서
해당 배열에서 뺀다.
여기서 answer = arr 후
arr.sort()를 하니 answer도 함께 바뀜. -> sorted() 쓰면 됨
'''

def solution(arr):
    min = arr[0]
    for i in arr:
        if min > i:
            min = i

    arr.remove(min)

    if len(arr) == 0:
        arr.append(-1)

    return arr

def solution2(arr):
    answer = arr
    number = sorted(arr, reverse=True)[-1]
    answer.remove(number)

    if len(answer) == 0:
        answer.append(-1)

    return answer
print(solution2([1, 5, 3, 4]))