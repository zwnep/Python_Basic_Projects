def sayınınTersiniBul(sayi,toplam):
    if sayi == 0:
        return toplam
    temp = sayi % 10 
    toplam = (toplam * 10) + temp
    return sayınınTersiniBul(sayi//10,toplam)

toplam = 0
sayi = int(input("Sayi Giriniz: "))
print("Girilen sayinin tersi: {}".format(sayınınTersiniBul(sayi,toplam)))