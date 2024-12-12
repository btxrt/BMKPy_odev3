urunler = ["iphone 13","samsung s24","samsung s22","iphone 15","iphone 14"]

#4- "urunler" listesindeki tüm iphone marka ürünleri listeleyiniz. (index ve find komutlarından faydalanınız.)

iphoneÜrünleri = []
for urun in urunler:
     if urun.find("iphone") !=-1:  #Eğer "iphone" kelimesi urun içinde bulunmazsa, find metodu -1 değerini döndürür.
         iphoneÜrünleri.append(urun)  #Append=listeye öğe ekler(sonuna)

print("Iphone ürünleri: " , iphoneÜrünleri)



# 5- "urunler" listesinde kaç adet samsung ürünü vardır? (find metodu)
samsungUrunler=[]

for urun in urunler:
    if urun.find("samsung") !=-1:
        samsungUrunler.append(urun)

samsungUrunSayısı=len(samsungUrunler)
print("Listede ", samsungUrunSayısı," adet sammsung ürün vardır.")

