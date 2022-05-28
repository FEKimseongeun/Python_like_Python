# ⭐️zip⭐️

## ****2차원 리스트 뒤집기****

[zip 함수](https://docs.python.org/3/library/functions.html?highlight=built%20function#zip) 를 이용해 2차원 배열을 뒤집는 방법을 알아보자

내 코드

```python
def solution(mylist):
    answer = [[0 for col in range(len(mylist[0]))] for row in range(len(mylist))]
    for i in range(len(mylist)):
        for j in range(len(mylist[i])):
            answer[i][j]=mylist[j][i]
    print(answer)
    return answer
```

보통은 다음과 같이 2중 for 문을 이용해 리스트의 row와 column을 뒤집습니다.

```python
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = [[], [], []]

for i in range(len(mylist)):
    for j in range(len(mylist[i])):
        new_list[i].append(mylist[j][i])
```

---

python에서는….

파이썬의 [zip](https://docs.python.org/3/library/functions.html?highlight=built%20function#zip) 과 **unpacking** 을 이용하면 코드 한 줄로 리스트를 뒤집을 수 있습니다.

```python
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist)))
```

### ****zip 함수에 대해****

[**파이썬 3 한글 번역 - zip**](https://docs.python.org/ko/3/library/functions.html?highlight=built%20function) 에 따르면

> **zip(*iterables)**는 각 **iterables 의 요소**들을 모으는 이터레이터를 만듭니다.

> **튜플**의 이터레이터를 돌려주는데, i 번째 튜플은 각 인자로 전달된 시퀀스나 이터러블의 i 번째 요소를 포함합니다.


```python
mylist = [1, 2, 3]
new_list = [40, 50, 60]
for i in zip(mylist, new_list):
    print (i)

#(1, 40)
#(2, 50)
#(3, 60)
```

- **사용 예 #1 - 여러 개의 Iterable 동시에 순회할 때 사용**

```python
list1 = [1, 2, 3, 4]
list2 = [100, 120, 30, 300]
list3 = [392, 2, 33, 1]
answer = []
for number1, number2, number3 in zip(list1, list2, list3):
   print(number1 + number2 + number3)

#493
#124
#66
#305
```

- **사용 예 #2 - Key 리스트와 Value 리스트로 딕셔너리 생성하기**

파이썬의 zip 함수와 dict 생성자를 이용하면 **코드 단 한 줄**로, 두 리스트를 합쳐 딕셔너리로 만들 수 있습니다.

```python
animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
answer = dict(zip(animals, sounds)) 

# {'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}
```

---

## ****i번째 원소와 i+1번째 원소****

보통은 다음과 같이 len과 index를 이용하여 각 원소에 접근

```python
def solution(mylist):
    answer = []

    for i in range(len(mylist)-1):
        answer.append(abs(mylist[i]-mylist[i+1]))

    print(answer)
    return answer
```

**python에서는….**

파이썬의 [zip](https://docs.python.org/3/library/functions.html?highlight=built%20function#zip)을 이용하면 index를 사용하지 않고 각 원소에 접근할 수 있다.

```python
def solution(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]):
        answer.append(abs(number1 - number2))
    return answer

mylist = [83, 48, 13, 4, 71, 11]    
print(solution(mylist))
```

‼ 주의 ‼ : **zip** 함수에 서로 길이가 다른 리스트가 인자로 들어오는 경우에는 길이가 짧은 쪽 까지만 이터레이션이 이루어집니다

- **array “::”**

    ```
    [0,1,2,3,4,5,6,7,8,9]
    >> arr[::2] # 처음부터 끝까지 두 칸 간격으로
    [0,2,4,6,8]
    >> arr[1::2] # index 1 부터 끝까지 두 칸 간격으로
    [1,3,5,7,9]
    >> arr[::-1] # 처음부터 끝까지 -1칸 간격으로 ( == 역순으로)
    [9,8,7,6,5,4,3,2,1,0]
    >> arr[::-2] # 처음부터 끝까지 -2칸 간격으로 ( == 역순, 두 칸 간격으로)
    [9,7,5,3,1]
    >> arr[3::-1] # index 3 부터 끝까지 -1칸 간격으로 ( == 역순으로)
    [3,2,1,0]
    >> arr[1:6:2] # index 1 부터 index 6 까지 두 칸 간격으로
    [1,3,5]
    ```