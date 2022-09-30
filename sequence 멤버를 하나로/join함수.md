## ****sequence 멤버를 하나로 이어붙이기 - join****

알고리즘 문제를 풀다보면, 시퀀스의 멤버들을 하나의 string으로 이어붙여야 할 때가 있다.

- 문자열 배열 `['1', '100', '33']`을 이어 붙여 문자열 '110033' 만들기
- 정수형 튜플 `(3, 22, 91)`을 이어붙여 문자열 '32291' 만들기

이런 경우에 말이다.

join을 쓰지 않는다면

```python
my_list = ['1', '100', '33']
answer = ''
for value in my_list:
    answer += value
```

이렇게 사용하곤 하는데

파이썬에서 제공하는 str.join(iterable)을 사용하면 더 줄일 수 있다!

```python
my_list = ['1', '100', '33']
answer = ''.join(my_list)
```