n = int(input())

a = [1 for _ in range(5)]

for i in range(n-1):
    b = [1]
    for i in range(1,5): 
        b.append(b[i-1] + a[i])
    a = b

print(max(a))


