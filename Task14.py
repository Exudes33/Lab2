a = int(input())
b = list(map(int, input().split()))


d = {}
for x in b:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1


m_v = 0
m_k = 0


for k, v in d.items():
    if v > m_v:
        m_v = v
        m_k = k
    elif v == m_v:
        if k < m_k:
            m_k = k

print(m_k)
