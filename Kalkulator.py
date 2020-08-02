#kalkulator

def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    return x / y

def pangkat(x, y):
	return x ** y

print("Pilih operasi yang akan digunakan.")
print("1.Pertambahan")
print("2.Pengurangan")
print("3.Perkalian")
print("4.Pembagian")
print("5.Perpangkatan")

while True:
    # ngambil input user
    choice = input("Masukan pilihan: (1/2/3/4/5): ")

    
    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Masukan angka pertama: "))
        num2 = float(input("Masukan angka kedua: "))

        if choice == '1':
            print(num1, "+", num2, "=", tambah(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", kurang(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", kali(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", bagi(num1, num2))
            
        elif choice == '5':
        	print(num1, "**", num2, "=", pangkat(num1, num2))
        break
    else:
        print("Invalid Input")
