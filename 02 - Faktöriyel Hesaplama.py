def faktöriyel(x):
    if x==0:
        return 1
    if x==1:
        return 1
    else:
        return x*faktöriyel(x-1)        

print(faktöriyel(5))