a = int(input())
d = {}

for i in range(a):
    s = input().split()
    name = s[0]      
    count = int(s[1])
  
    if name in d:
        d[name] += count
    else:
        d[name] = count
b = sorted(d.keys())


for x in b:
    print(x, d[x])
