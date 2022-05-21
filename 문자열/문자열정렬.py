s, n = input().strip().split(' ')
n = int(n)
answer = ''
### 좌측 정렬 예
for i in range(len(s)-n): # 문자열의 앞을 빈 문자열로 채우는 for 문
    answer += ' '
answer += s
print(answer)
answer = ''

### 중앙 정렬 예
for i in range(len(s)//2+1): # 문자열의 앞을 빈 문자열로 채우는 for 문
    answer += ' '
answer += s
print(answer)
answer = ''

### 우측 정렬 예
for i in range(n-len(s)): # 문자열의 앞을 빈 문자열로 채우는 for 문
    answer += ' '
answer += s

print(answer)



#s.ljust(n) # 좌측 정렬
#s.center(n) # 가운데 정렬
#s.rjust(n) # 우측 정렬