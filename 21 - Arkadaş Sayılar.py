# ARKADAŞ SAYILAR ->İki sayı birbirinin kendisi hariç bölenleri toplamına eşitse bu sayılara arkadaş sayılar denir.

# Örnek: 220 ve 284

# 220 : 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284 284 : 1 + 2 + 4 + 71 + 142 = 220 

n1 = int(input('Birinci Sayıyı Giriniz...:'))
n1Sum = 0
n2 = int(input('İkinci Sayıyı Giriniz...:'))
n2Sum = 0

def areFriends(n1,n2,n1Sum,n2Sum):
  for i in range(1, n1):
    if n1 % i == 0:
      n1Sum += i
      
  for j in range(1, n2):
    if n2 % j == 0:
      n2Sum += j


  if (n1Sum == n2 and n2Sum == n1):
    print('Girilen İKİ sayı Arkadaştır...:', n1, n2)
  else:
    print('TEKRAR DENEYİNİZ...')

areFriends(n1,n2,n1Sum,n2Sum)