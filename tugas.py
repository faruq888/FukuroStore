print("\n-------Fukuro Store-------")
pembeli = input("\nMasukkan Nama Pembeli: ")
print("Nama Pembeli:",pembeli)

def fungsimakanan():
    global totalmkn
    global porsi
    global mkn
    print("\n-----MENU MAKANAN-----\n")
    print("1. Mie Ayam ----- Rp. 12000")
    print("2. Kwetiau ----- Rp. 15000")
    print("3. Seblak ----- Rp. 12000")
    print("4. Bakmie ----- Rp. 12000")
    print("5. Lalapan Ayam ----- Rp. 10000")
    nomor=int(input("\nMasukkan Pilihan: "))
    porsi= int(input("Berapa Porsi: "))
    if nomor==1: 
        totalmkn=porsi*12000
        print (porsi,"porsi Mie Ayam = Rp",totalmkn)
        mkn=("Mie Ayam")
    elif nomor==2:
        totalmkn=porsi*15000
        print (porsi,"porsi Kwetiau = Rp",totalmkn)
        mkn=("Kwetiau")
    elif nomor==3:
        totalmkn=porsi*12000
        print (porsi,"Seblak = Rp",totalmkn)
        mkn=("Seblak")
    elif nomor==4:
        totalmkn=porsi*12000
        print (porsi, "porsi Bakmie = Rp",totalmkn)
        mkn=("Bakmie")
    elif nomor==5:
        totalmkn=porsi*10000
        print (porsi, "porsi Lalapan Ayam = Rp",totalmkn)
        mkn=("Lalapan Ayam")
    else:
        print("Pilihan tidak ada, silahkan masukkan lagi!")
        fungsimakanan()
def fungsiminuman():
    global totalmnm
    global mnm
    global gelas
    print("\n-----MENU MINUMAN-----\n")
    print("1. Air Bening --- Rp 3000")
    print("2. Es Teh Manis --- Rp 3000")
    print("3. Teh Hangat Manis --- Rp.3000")
    print("4.Es Kopi Susu --- Rp 8000")
    print("5. Es Jeruk --- 5000")
    nomor=int(input("\nMasukkan Pilihan: "))
    gelas= int(input("Berapa Gelas: "))
    if nomor==1: 
        totalmnm=gelas*3000
        print (gelas,"Air Bening = Rp",totalmnm)
        mnm=("Air Bening")
    elif nomor==2:
        totalmnm=gelas*3000
        print (gelas,"Es Teh Manis = Rp",totalmnm)
        mnm=("Es Teh Manis")
    elif nomor==3:
        totalmnm=gelas*3000
        print (gelas,"Teh Hangat Manis = Rp",totalmnm)
        mnm=("Teh Hangat Manis")
    elif nomor==4:
        totalmnm=gelas*8000
        print (gelas, "Es Kopi Susu = Rp",totalmnm)
        mnn=("Es Kopi Susu")
    elif nomor==5:
        totalmnm=gelas*5000
        print (gelas, "Es Jeruk = Rp",totalmnm)
        mnm=("Es Jeruk")
    else:
        print("Pilihan tidak ada, silahkan masukkan lagi!")
        fungsiminuman()
        
fungsimakanan()
fungsiminuman()
totalsemua= totalmkn + totalmnm

print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian: ",kembalian)
print("\n=====================")
print("=======STRUK BELI=======")
print("=====================")
print("Nama\t\t:",pembeli)
print("Beli\t\t:",porsi,mkn,"(Rp",totalmkn,")")
print("\t\t",gelas,mnm,"(Rp",totalmnm,")")
print("Tagihan\t\t: Rp",totalsemua)
print("Dibayar\t\t:Rp",uang)
print("Kembalian\t:RP",kembalian)
print("=================================")
print("=================================")

print("\n\n\nTerima Kasih")

        
                
        