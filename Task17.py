a = int(input())

d = {}

for i in range(a)
    s = input().strip()
    
    if s in d:
        d[s] += 1
    else:
        d[s] = 1
c = 0

for v in d.values():
    if v == 3:
        c += 1

print(c)
