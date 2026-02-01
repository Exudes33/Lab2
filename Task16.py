a = int(input())

b = list(map(int, input().split()))

s = set()

for x in b:
    if x in s:
        print("NO")
    else:
        print("YES")
        s.add(x)
