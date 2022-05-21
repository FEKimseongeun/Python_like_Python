# n진법으로 표기된 string을 10진법 숫자로 변환하기 - int 함수

예시) 5진법으로 적힌 문자열 '3212'를 10진법으로 바꾸기

보통 사람들은 for 문을 이용해 숫자를 곱해가며 문제를 푼다.

```python
num = '3212'
base = 5

answer = 0
for idx, number in enumerate(num[::-1]):
    answer += int(number) * (base ** idx)
```

파이썬에서는..

### [int(x, base=10)](https://docs.python.org/3/library/functions.html#int) 함수는 진법 변환을 지원

```python
num = '3212'
base = 5
answer = int(num, base)
```