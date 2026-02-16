n = int(input())
a = list(map(int, input().split()))

count_max = 0
answer = a[0]

for x in a:
    count = 0
    for y in a:
        if x == y:
            count += 1
            
    if count > count_max:
        count_max = count
        answer = x
    elif count == count_max and x < answer:
        count_max = count
        answer = x

print(answer)
