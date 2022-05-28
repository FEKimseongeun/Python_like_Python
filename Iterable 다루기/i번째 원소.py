# def solution(mylist):
#     answer = []
#
#     for i in range(len(mylist)-1):
#         answer.append(abs(mylist[i]-mylist[i+1]))
#
#     print(answer)
#     return answer

def solution(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]):
        answer.append(abs(number1 - number2))
    return answer


solution([83, 48, 13, 4, 71, 11])