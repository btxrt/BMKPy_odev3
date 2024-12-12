sayilar = [3,5,7,2,12,32,45]

# 1- "sayilar" listesindeki her bir elemanı yazdırınız.

for x in sayilar:
    print(x)

# 2- "sayilar" listesinde hangi sayılar 3' ün katıdır?

print("listedeki 3 ün katı olan sayılar=")

for n in sayilar:
    if n % 3 == 0:
        print(n)

# 3- "sayilar" listesinde tüm sayıların toplamı nedir?


print("listedeki sayıların toplamı= " + str(sum(sayilar)))

