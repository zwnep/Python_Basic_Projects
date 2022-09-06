#Bir liste içindeki 5'in katları olan sayıları bulan ve ekrana yazdıran program.

def list(liste):
    list2=[]
    for sayi in liste:
        if sayi%5==0:
            list2.append(sayi)
    print(list2)        

liste=[2,5,17,87,225,55,67,24,83]
list(liste)