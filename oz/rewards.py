a = list(map(int, input().split()))
b = list(map(int, input().split()))
n = int(input())

a_ = sum(a)//5 if sum(a)%5 == 0 else sum(a)//5 + 1
b_ = sum(b)//10 if sum(b)%10 == 0 else sum(b)//10 + 1

answer = 'YES' if a_ + b_ <= n else 'NO'
print(answer)