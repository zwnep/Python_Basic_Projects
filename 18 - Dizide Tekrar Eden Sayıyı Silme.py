
#Dizide Tekrar Eden Değerleri Silme

def removeDuplicates(liste):
    removed_list = []
    if liste:
        for item in liste:
            if item not in removed_list:
                removed_list.append(item)
    else:
        return liste
    print("Fazlalıklardan kurtulmuş yeni dizi: {}".format(removed_list))

liste = [1,2,2,3,4,1,7,4,8,7,3]
removeDuplicates(liste)