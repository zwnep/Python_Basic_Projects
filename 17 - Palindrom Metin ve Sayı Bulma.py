
#Palindrom kelime ve sayı bulma

def Ters(kelimeOrSayi):
    return kelimeOrSayi[::-1]

def Palindrom(kelimeOrSayi):
    ters = Ters(kelimeOrSayi)
    if ters == kelimeOrSayi:
        print("PALİNDROM")
    else:
        print("PALİNDROM; değil.")    

kelimeOrSayi = input("Kelime veya sayı girişi yapın: ")
sonuc = Palindrom(kelimeOrSayi)

