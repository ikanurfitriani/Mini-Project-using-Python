print('*'*32)
print("MENENTUKAN BILANGAN GANJIL GENAP")
print('*'*32)

bil = int(input("Masukan Bilangan : "))

if bil % 2 == 0:
    print("%d merupakan bilangan Genap" % bil)
else:
    print("%d merupakan bilangan Ganjil" % bil)