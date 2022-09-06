#Facebook Interview Question!
# Parametre olarak bir tamsayı dizisi alan bir fonksiyon yazın (fonksiyonun adi moveZeroes olsun). Bu fonksiyonun görevi bu tamsayı dizisindeki sıfır olmayan öğelerin göreli sırasını korurken, tüm 0'ları dizinin sonuna taşısın.

# Not: Bunu dizinin bir kopyasını oluşturmadan, aynı dizi üzerinde yapmanız gerekmektedir.

# Örnek:
# sayilar = [0,1,0,3,11]
# moveZeroes(sayilar)
# print(sayilar)  => Ekrana [1, 3, 11, 0, 0] yazmalı.

def moveZeroes(numbers):
    j = 0
    length = len(numbers)
    for num in numbers:
        if num!=0:
            numbers[j]=num
            j+=1
    for i in range(j,length):
        numbers[i]=0
    print(numbers)

numbers=[12,0,5,8,0,0,21]
moveZeroes(numbers)    