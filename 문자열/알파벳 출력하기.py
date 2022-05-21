# 문제 설명
# 입력으로 0이 주어지면 영문 소문자 알파벳을,
# 입력으로 1이 주어지면 영문 대문자 알파벳을 사전 순으로 출력하는 코드를 짜세요.
num = int(input().strip())
if num==0:
    for x in range(97,123):
        print(chr(x),end="")
if num==1:
    for x in range(65,91):
        print(chr(x),end="")


#import string
# string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
# string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.digits # 숫자 0123456789