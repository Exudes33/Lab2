a = int(input())
b = list(map(int, input().split()))

m = b[0]
pos = 0

for i in range(a):
    if b[i] > m:
        m = b[i]
        pos = i

print(pos+1)
