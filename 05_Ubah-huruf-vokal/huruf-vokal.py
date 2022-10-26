print('*'*20)
print("MENGUBAH HURUF VOKAL")
print('*'*20)

teks = input('Ketik sesuatu: ')
pengganti = input('Masukkan pengganti huruf vokal: ')

for huruf in 'aiueoAIUEO':
  teks = teks.replace(huruf, pengganti)

print(f'\n{teks}')