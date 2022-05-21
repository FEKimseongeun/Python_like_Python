s, n = input().strip().split(' ')
n = int(n)

left=right=mid=[0 for i in range(n)]
for i in range(len(s)):
    left.insert(i, s[i])

for i in range(len(s)):
    mid.insert(n//2+i, s[i])

for i in range(len(s)):
    right.append(s[i])

print(left, mid, right)