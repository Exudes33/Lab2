a, b, c = map(int, input().split())

d = list(map(int, input().split()))

d[b-1:c] = d[b-1:c][::-1]

print(*d)
