# Öğrencilerine 12 haneli öğrenci numarası veren üniversitenin verdiği numaranın ilk 4 hanesi giriş yılı 5. ve 6. hanesi okuduğu fakültenin numarası 7. ve 8. hane bölüm numarası 9. hanesi öğrenim numarası 11. ve 12. hane ise öğrencinin üniversiteye giriş sırasıdır. 12 haneli öğrenci kodunu kullanıcıdan alarak anlamlı şekilde ayıran ve ekrana yazan kodu yazınız.
            
# Örnek Çıktı:
# Öğrenci No: 20151411321
# NUMARANIN ACILIMI:
# GirisYili: 2015
# FokulteNo: 14
# BolumNo: 11
# OgrenimNo: 3
# OgrenciNo: 21

def ogrenciTespiti(numara):
    no=str(numara)
    ogrInfo=dict(girisYili=no[:4],
    fakulteNo=no[4:6],
    bolumNo=no[6:8],
    ogrenciNo=no[8:9],
    ogrGirisSırası=no[10:12])
    print("Girilen numaranın açılımı: \n")
    for i in ogrInfo.items():
        print(i[0] + ":" + i[1])

ogrenciTespiti(20151411321)