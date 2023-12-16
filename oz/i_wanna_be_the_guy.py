n = int(input())
x = set(map(int, input().split()))
y = set(map(int, input().split()))

answer = 'I become the guy' if x.union(y) == set(range(1,n+1)) else 'Oh, my keyboard'

print(answer)
    