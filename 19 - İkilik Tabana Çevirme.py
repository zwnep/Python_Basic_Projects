
#Bir Sayının İkli Tabadaki Değerini Hesaplama

def binary(sayi):
    if sayi > 1:
        binary(sayi//2)
    print(sayi % 2, end = " ")    

deger = int(input("Bir Değer Giriniz: "))
print("{} sayısının ikilik tabandaki değeri: ".format(deger))
binary(deger)
