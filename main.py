from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
import base64

# Qelesi
KEY = b"1234567890abcdef12345678"
KEY = DES3.adjust_key_parity(KEY)


# Teksti

def enkripto_tekst():
    message = input("Shkruaj tekstin: ")

    cipher = DES3.new(KEY, DES3.MODE_CBC)
    iv = cipher.iv

    padded = pad(message.encode("utf-8"), DES3.block_size)
    encrypted = cipher.encrypt(padded)

    result = base64.b64encode(iv + encrypted).decode("utf-8")

    print("\nTeksti i enkriptuar:")
    print(result)


def dekripto_tekst():
    encrypted_input = input("Shkruaj tekstin e enkriptuar (Base64): ")

    try:
        data = base64.b64decode(encrypted_input)

        if len(data) < 8:
            print("Input i pavlefshëm!")
            return

        iv = data[:8]
        encrypted = data[8:]

        cipher = DES3.new(KEY, DES3.MODE_CBC, iv=iv)
        decrypted = unpad(cipher.decrypt(encrypted), DES3.block_size)

        print("\nTeksti i dekriptuar:")
        print(decrypted.decode("utf-8"))

    except Exception as e:
        print("Gabim gjatë dekriptimit:", e)


#Fajllat

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

        print("\nFajlli u enkriptua me sukses!")
        print("Fajlli i ri:", output_name)

    except Exception as e:
        print("Gabim:", e)


def dekripto_fajll():
    file_name = input("Shkruaj emrin e fajllit të enkriptuar: ")

    try:
        with open(file_name, "rb") as f:
            data = f.read()

        if len(data) < 8:
            print("Fajll i pavlefshëm!")
            return

        iv = data[:8]
        encrypted = data[8:]

        cipher = DES3.new(KEY, DES3.MODE_CBC, iv=iv)
        decrypted = unpad(cipher.decrypt(encrypted), DES3.block_size)

        output_name = "decrypted_" + file_name.replace("encrypted_", "")

        with open(output_name, "wb") as f:
            f.write(decrypted)

        print("\nFajlli u dekriptua me sukses!")
        print("Fajlli i ri:", output_name)

    except Exception as e:
        print("Gabim gjatë dekriptimit:", e)


# Menu kryesor

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