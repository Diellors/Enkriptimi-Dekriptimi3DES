from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import base64

KEY = b"1234567890abcdef12345678"
KEY = DES3.adjust_key_parity(KEY)

def enkripto_tekst():
    message = input("Shkruaj tekstin: ")
    cipher = DES3.new(KEY, DES3.MODE_CBC)
    iv = cipher.iv

    padded = pad(message.encode(), DES3.block_size)
    encrypted = cipher.encrypt(padded)

    result = base64.b64encode(iv + encrypted).decode()
    print("\nTeksti i enkriptuar:", result)
    

def enkripto_fajll():
    file_name = input("Shkruaj emrin e fajllit: ")
    try:
        with open(file_name, "rb") as f:
            data = f.read()
        cipher = DES3.new(KEY, DES3.MODE_CBC)
        iv = cipher.iv

        encrypted = cipher.encrypt(pad(data, DES3.block_size))
        output_name = "encrypted_" + file_name
        with open(output_name, "wb") as f:
            f.write(iv + encrypted)


        print("Fajlli u lexua me sukses!")
    except Exception as e:
        print(f"Gabim: {e}")

        





while True:
    print("\n--- 3DES MENU ---")
    print("1. Enkripto Tekst")
    print("2. Enkripto Fajll")
    print("3. Dekripto Tekst")
    print("4. Dekripto Fajll")
    print("0. Dil")

    zgjedhja = input("Zgjedhja: ")

    if zgjedhja == "1":
        enkripto_tekst()
    elif zgjedhja == "2":
        enkripto_fajll()
    elif zgjedhja == "3":
        dekripto_tekst()
    elif zgjedhja == "4":
        dekripto_fajll()
    elif zgjedhja == "0":
        print("Programi u mbyll.")
        break
    else:
        print("Opsion i pavlefshëm!")