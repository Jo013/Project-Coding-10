import os
import random
import string
os.system("cls")

Data = dict()
while True:
    os.system("cls")
    
    Key1 = "".join(random.choice(string.ascii_uppercase) for i in range(3))
    print(f" Current Key : {Key1}\n")
    print(f"{ " Data Pemilihan Ketua Kelas ":–^56}\n")
    
          
          
    Name   = input(" ⟪ Masukkan Nama ⟫ \n →  ")
    print("\n")
    Absen  = input(" ⟪ Masukkan Nomor Absen ⟫\n →  ")
    print("\n")     
    os.system("cls")
  

  
    print(f"{ " Data Pemilihan Ketua Kelas ":–^56}\n")
    print('''
    Kandidat :
    1. Jason 🔷
    2. Aman 🐟
    3. Sara 🌸
          ''')
    print("–"*56,"\n")
          


    Vote   = int(input(" ⟪ Masukkan Pilihan (1-3) ⟫\n → "))
    if Vote == 1:
        Vote = 'Jason'
        Emoji = '🔷'
    elif Vote == 2:
        Vote = 'Aman'
        Emoji = '🐟'
    elif Vote == 3:
        Vote = 'Sara'
        Emoji = '🌸'
    else:
        break



    print("–"*56)
    Data[Key1] = {'NameKey' : Name, 'Absen' : Absen, 'Vote' : Vote }
    os.system("cls")
    print(f"{ " Data Pemilihan Ketua Kelas ":–^56}\n")
    Answer = input(" Vote ulang? (Y/N)            : ").upper()
    if Answer == "N":
        os.system("cls")
        print(f"{ " Data Pemilihan Ketua Kelas ":–^56}\n")
        print(f"\t\t {Emoji}{ " TERIMA KASIH :) " }{Emoji}\n\n")
        break
    else:
        continue
    


print(f" KEY\t  NAMA\t\t ABSEN\t\t    VOTE")
print("–"*56)
for key, value in Data.items():
    print(f" {key}\t {Data[key]['NameKey']}\t\t  {Data[key]['Absen']}\t\t    {Data[key]['Vote']}")         