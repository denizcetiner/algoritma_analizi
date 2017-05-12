from random import random

kume = [random() for i in range(10)]
veri = [random() for i in range(1000)]

parametre = 0.01  #min 0 max 1

for x in veri:  # O(veri sayisi)
    enyakinK= 0;
    enkucukHata = 9999; 
    for k in enumerate(kume):  # O(mean sayısı)
        hata = abs(x-k[1])
        if hata < enkucukHata:
            enkucukHata = hata
            enyakinK = k[0]
        kume[enyakinK] = kume[enyakinK]*(1-parametre) + x*(parametre)

print (kume)

karmaşıklık O(data*means) yani Veri sayısı = K ve Küme Sayısı = J için  O(K.J) 
