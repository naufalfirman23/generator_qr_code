import pyqrcode
import pandas as pd 



def Gen_QrCode_Csv() :
    inputanfile = input('Masukan Nama File CSV : ')

    nama_file = inputanfile+'.csv'
    data =  pd.read_csv(nama_file,delimiter=';')
    for index , row in data.iterrows() :
        npm = row['NPM']
        nama = row['NAMA'] 
        # Created Qr-Code
        pngname = 'QrCode'+f'-{nama}'+'.png'
        stts = 'succes'
        qr = pyqrcode.create(str(npm))
        stts = 'succes'
        qr.png(pngname, scale=8)
        stts = 'succes'

    if stts == 'succes' :
        print(stts)
    else :
        print("Not Succes Created Qr-Code")

def Gen_QrCode_Manual():
    data = input("Masukan Text Yang Akan di Generate : ")
    namefile = input("Masukan Nama File Qr-Code : ")
    namepng = namefile+".png"
    qr = pyqrcode.create(str(data))
    qr.png(namepng, scale=8)


def menu():
    print(f'''
########## PILIH MENU ##########

1. Qr-Code File CVS
2. Qr-Code Text 
3. Back To Menu

--Pres Q and Enter For Quit--

''')


while True :
    menu()
    choose = str(input("Masukan Menu Pilihan anda : "))
    if choose == '1' :
        Gen_QrCode_Csv()
    elif choose == '2' :
        Gen_QrCode_Manual()
    elif choose == '3' :
        menu()
    elif choose == 'q':
        break






