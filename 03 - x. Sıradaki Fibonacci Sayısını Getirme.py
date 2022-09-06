#1,1,2,3,5,8,13,21,34,55,89,144,233,377.....

# x. sıradaki fibonacci sayısını getirme

def fibonacci(x):
    if x==1:
        return 1
    if x==2:
        return 1
    else:
        return fibonacci(x-1)+fibonacci(x-2)

print(fibonacci(6))   
