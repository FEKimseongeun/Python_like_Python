def solution(mylist):
    answer = []
    for num in mylist:
        answer.append(int(num))
    return answer

mylist=['1', '100', '33']
print(solution(mylist))