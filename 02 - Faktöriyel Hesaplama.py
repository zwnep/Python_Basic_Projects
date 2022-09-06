def factorial(x):
    if x < 0:
        return 'Not defined'
    elif x==0:
        return 1
    else:
        factorial = 1
        for i in range(1, x+1):
            factorial = factorial * i
        return factorial

print(factorial(5))
