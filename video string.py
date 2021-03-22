'''
Edwin Mahendra 71200541 - STRING

buatlah program untuk mengetahui kata ada di kalimat ke berapa,
menyisipkan karakter, atau membalik kata. jika user menginputkan
pilihan selain 1,2, dan 3. maka akan muncul output pilihan anda tidak ada di menu.

input:
kalimat=input()
pilihan=input()

proses dan output:
if pilihan =1:
    splt=kalimat.split()
    y=input(masukkan karakter sisipan)
    repl=y.join(splt)
    print(repl)
    contoh:
    aku sayang kamu
    aku*sayang*kamu
elif pilihan =2:
    splt=kalimat.split()
    c=input(masukkan kata yang dicari)
    a=0
    for i in range(len(split)):
        if c==splt[i]:
            a=i
    if c in splt:
        print(c,'ada di kata nomer',a)
    else:
        print(kata yang dicari tidak ad di menu)
elif pilihan =3:
    splt=kalimat.split()
    for i in(splt):
        print(' ',join(i.split()[::-1]))
    aku sayng kmu
    kmu sayng aku
else:
    print('pilihan anda tidak ad di menu)
'''
kalimat=input('masukkan kalimat:')
pilih=input('masukka pilihan:')

splt=kalimat.split()

if pilih=='1':
    y=input('masukkan karakter sisipan: ')
    repl=y.join(splt)
    print(repl)
elif pilih=='2':
    c=input('masukkan kata yang ingin dicari: ')
    a=0
    for i in range(len(splt)):
        if c==splt[i]:
            a=i
    if c in splt:
        print(c,'ada di kata nomer',a+1)
    else:
        print('maaf kata yang anda cari tidak ada')
elif pilih=='3':
    a=kalimat.split('\n')
    for i in(a):
        print(' '.join(i.split()[::-1]))
else:
    print('pilihan anda tidak ada di menu')