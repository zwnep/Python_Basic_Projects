# üs alma - çarpa bölme kullanmadan

# 5^6 işlemi için;

# 1.) 5 kere 5 ekle (5^2) = 25
# 2.) 5 kere 25 ekle (5^3) = 125
# 3.) 5 kere 125 ekle (5^4) = 625
# 4.) 5 kere 625 ekle (5^5) = 3125
# 5.) 5 kere 3125 ekle (5^6) = 15625

def us_alma(sayi,us):
    sonuc=sayi
    artıs=sayi
    if us==0:
        print(0)
    for i in range(1,us):
        for j in range(1,sayi):
            sonuc+=artıs
        artıs=sonuc    
    print("{} üssü {} : {}".format(sayi,us,sonuc))        
us_alma(5,3)    