x = int(input())

fib = [1, 1]
fib1, fib2 = fib

while fib2 < x:
    fib1, fib2 = fib2, fib1 + fib2
    fib.append(fib2)

a = ['O' if i in fib else 'o' for i in range(1, x+1)]
print(''.join(a))