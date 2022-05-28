def solution(mylist):
    answer = [[0 for col in range(len(mylist[0]))] for row in range(len(mylist))]
    for i in range(len(mylist)):
        for j in range(len(mylist[i])):
            answer[i][j]=mylist[j][i]
    print(answer)
    return answer

#--------------------------------------------------
# list1 = [1, 2, 3, 4]
# list2 = [100, 120, 30, 300]
# list3 = [392, 2, 33, 1]
# answer = []
# for number1, number2, number3 in zip(list1, list2, list3):
#     print(number1 + number2 + number3)