def fibonacci(x):
    if x==1 or x==0:
        return 1
    else:
        return fibonacci(x-2) + fibonacci(x-1)
 
fib = []

for i in range(20):
    fib.append(fibonacci(i)) 

print("The first", len(fib), "numbers of the Fibonacci sequence are: \n", fib)
print()
