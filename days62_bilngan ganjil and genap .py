angka = int (input("masukkan angka :"))

if angka % 2 == 0 :
    for i in range (2,angka+1,2):
        print (i, end = " ")
elif angka % 2 != 0 :
    for i in range (1, angka+2, 2):
        print ( i )

             
