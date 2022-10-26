print('*'*48)
print("MENENTUKAN MEAN MEDIAN MODUS DAN STANDAR DEVIASI")
print('*'*48)

from statistics import mean, median, multimode, stdev

lst = [int(item) for item in input("Masukan data angka (Pisahkan dengan spasi!) :\n").split()]
print("\nData yang Anda masukkan:")
print(*lst, sep = ", ")
print("Banyak data: " + str(len(lst)))

print("\nMEAN = " + str(mean(lst)))
print("MEDIAN = " + str(median(lst)))

modus = multimode(lst)
print("MODUS = ", end = "")
print(*modus, sep = ", ", end = " ")
if (len(modus) > 1):
   print("(multimodal)")
else:
   print("(modus tunggal)")

print("STANDAR DEVIASI = " + str(stdev(lst)))