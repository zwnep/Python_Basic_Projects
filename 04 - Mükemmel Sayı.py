#Mükemmel sayı -> Matematikte bazı pozitif tam sayıların pozitif bölenleri toplamı, sayının kendisinin iki katına eşittir.

def mükemmel_sayi(sayi):
    toplam=0
    for i in range(1,sayi+1):
        if sayi%i==0:
            toplam+=i
    if toplam==(sayi*2):
        print("girilen sayı mükemmel sayıdır.")
    else:
        print("girilen sayı mükemmel sayı değildir.\nbaşka bir sayı giriniz.")    

mükemmel_sayi(6)
mükemmel_sayi(7)