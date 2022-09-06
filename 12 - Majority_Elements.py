#Majority Elements -> dizide çoğunlukta bulunan dizi elemeninin sayısı dizi boyutunundan(n) n/2 fazla olması

def findMajority(arr):
    maxCount = 0
    arrLengt = len(arr)
    index = -1
    for i in range(arrLengt):
        count = 0
        for j in range(arrLengt):
            if arr[i] == arr[j]:
                count += 1
        if count > maxCount:
            maxCount = count   
            index = i
    if (maxCount > arrLengt//2):            
        print(arr[index])
    else:
        print("NO MAJORITY ELEMENT")    


arr=[1,1,2,1,3,5,1]
findMajority(arr)