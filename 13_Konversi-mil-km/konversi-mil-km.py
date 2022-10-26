print('*'*30)
print("KONVERSI MIL --><-- KILOMETER")
print('*'*30)

# import module
import os
import platform
import math
 
# konversi kilometer ke mil
def conv_kilometer(kilometer):
    faktor_konversi = 0.621371
    mil = kilometer * faktor_konversi
    return mil
 
# konversi mil ke kilometer
def conv_miles(mil):
    faktor_konversi = 0.621371
    kilometer = mil / faktor_konversi
    return kilometer
 
def main():
    # main menu
    print("1. Konversi Mil ke Kilometer")
    print("2. Konversi Kilometer ke Mil")
 
    choice = int(input('Masukan Pilihan: '))
 
    if choice == 1:
        number = float(input('Masukan Satuan Jarak (Mil): '))
        conv_miles(number)
        print(f'\nHasil Konversi dari {number} Mil adalah {conv_miles(number)} Kilometer')
 
    elif choice == 2:
        number = float(input('Masukan Jarak Satuan (Kilometer): '))
        conv_kilometer(number)
        print(f'\nHasil konversi dari {number} Kilometer adalah {conv_kilometer(number)} Mil')
 
    else:
        sistem_operasi = platform.system()
        if sistem_operasi == 'Linux':
            os.system('clear')
        elif sistem_operasi == 'Windows':
            os.system('cls')
        else:
            pass
 
        print('Pilih input yang Benar [1 / 2]')
        main()
 
 
if __name__=='__main__':
    main()