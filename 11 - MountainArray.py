#Microsoft Interview Question!
# Parametre olarak bir tamsayı listesi/arrayi (lst) alan bir fonksiyon yazın (fonksiyonun adı validMountainArray olsun). 
# Bu fonksiyonun görevi lst tamsayı listesi eğer geçerli bir mountain array ise true değerini döndürsün aksi halde false değerini döndürsün.

# Yani tekrar etmek gerekirse liste içindeki sayılar önce artacak daha sonra azalacaklardır.

# Sadece artma veya sadece azalma mountain array olmamaktadır.

# Bilgi: Mountain Array dizisi tanımı:

# lst.length >= 3 OLMALI

# i with 0 < i < lst.length - 1 öyle ki:

# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]

# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

# Örnek:
# Input: lst = [3,1]
# Output: false
 
# Input: arr = [3,4,4]
# Output: false
 
# Input: arr = [0,4,2,1]
# Output: true

def validMountainArray(lst):
    lenght=len(lst)
    if lenght>=3:
        #Arrayin yükselen kısmının bittiği noktayı bulundu.
        i = 1
        while (i<lenght and lst[i]>lst[i-1]):
            i+=1
        
        #Dizinin sonuna geldiysek sadece yükselme işlemi var alçalan kısım yok False döndür..      
        if (i==1 or i==lenght):
            print("FALSE")

        #Arrayin azalan kismina bakaldı nereye kadar azalma olacak.     
        while (i<lenght and lst[i]<lst[i-1]):
            i+=1

        # Eğer alçalan kısmın bitişi dizinin sonu ise bu bir Mountain Array'dir..
        # Aksi takdirde tekrar bir yükselme veya eşitlik olacaktır ki Mountain Array tanımına uymaz.
        if (i==lenght):
            print("TRUE")
        else:
            print("ELSE")    
    else:
        print("FALSE")

lst=[0,1,4,9,5,3,2]
validMountainArray(lst)
