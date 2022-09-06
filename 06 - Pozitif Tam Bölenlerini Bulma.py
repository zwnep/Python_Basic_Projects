#pozitif tam bölenlerini bulma
# pozitif tam bölenlerin sayını bulmak demek, herhangi bir sayıyı kalansız olarak bölen sayıların toplam adedini bulmak demek.

def Pozitif_tam_bolen(sayi):
    adet=0
    for i in range(1,sayi+1):
        if sayi%i==0:
            adet+=1
            print(i)
    print("pozitif tam sayıların adedi: {}".format(adet))    

Pozitif_tam_bolen(9)