#Babil Methodu ile Karekök Bulma: 

# e = hata değeri

def karekok_babil(sayi,e):
    y = 1
    x = sayi
    while (x - y > e) :
        x=(x+y)/2
        y=sayi/x
    print("{} sayısının karakökü: {}\n doğruluk seviyesi: {} ".format(sayi,x,e))

karekok_babil(36,0.000000000001) 