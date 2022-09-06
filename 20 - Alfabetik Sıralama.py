# Girilen kelimeyi , alfabetik sıraya göre düzenleyen program 
data = input('Yazı Giriniz...:')
txt = []
newTxt = ''
for k in range(len(data)):
    txt.append(ord(data[k]))

for i in range(len(txt)):
    for j in range(len(txt) - 1):
       if txt[j] > txt[j + 1]:
           A = txt[j]
           txt[j] = txt[j + 1]
           txt[j + 1] = A


print('Girilen Metin...:', data)
for x in range(len(txt)):
    newTxt += chr(txt[x])

print('Sonuç...:', newTxt)