# Girilen Kelimenin bütün kombinasyonları ile yazılması 

txt = input('Kelime Giriniz...:')
dizi = []
for k in range(len(txt)):
    dizi.append(txt[k])
    
for i in range(len(dizi)):
    for j in range(len(dizi), 0 , -1):
        print(dizi[i-j], end="")
    print('')