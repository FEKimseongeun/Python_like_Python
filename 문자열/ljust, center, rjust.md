# ljust, center, rjust

> ****문자열 정렬하기 - ljust, center, rjust****
>

```
'가나다라               ' # 좌측정렬
'               가나다라' # 우측 정렬
'       가나다라        ' # 가운데 정렬
```

보통 사람들은 for 문을 이용해 기존 스트링에 공백문자 (' ') 를 여러 번 붙이는 번거로운 일을 한다.

```python
### 우측 정렬 예
s = '가나다라'
n = 7

answer = ''
for i in range(n-len(s)): # 문자열의 앞을 빈 문자열로 채우는 for 문
    answer += ' '
answer += s
```

파이썬에서는 **[ljust](https://docs.python.org/3/library/stdtypes.html?highlight=rjust#str.ljust), [center](https://docs.python.org/3/library/stdtypes.html?highlight=rjust#str.center), [rjust](https://docs.python.org/3/library/stdtypes.html?highlight=rjust#str.rjust)** 와 같은 **string의 메소드**를 사용해 코드를 획기적으로 줄일 수 있다.

```python
s = '가나다라'
n = 7

s.ljust(n) # 좌측 정렬
s.center(n) # 가운데 정렬
s.rjust(n) # 우측 정렬
```