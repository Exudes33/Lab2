a = int(input())
d = {}

for i in range(1, a + 1):
    s = input().strip()
    if s not in d:
        d[s] = i       
b = sorted(d.keys())


for x in b:
    print(x, d[x])
