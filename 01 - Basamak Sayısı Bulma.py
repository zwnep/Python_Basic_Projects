def basamak_sayı_bul(sayi):
    sayac=0
    while sayi>=10:
        sayac+=1
        sayi=sayi/10
    sayac+=1    
    print("basamak sayısı: "+str(sayac))
    
basamak_sayı_bul(12343) 
