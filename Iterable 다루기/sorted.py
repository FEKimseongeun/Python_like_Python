list1 = [3, 2, 5, 1]
list2 = [i for i in list1] # 또는 copy.deepcopy를 사용
list2.sort()

list3 =[3, 2, 5, 1]
list4 = sorted(list3)
print(list2)
print(list4)