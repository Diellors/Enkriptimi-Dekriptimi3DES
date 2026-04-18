from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
import base64

# Çelësi sekret (24 byte)
KEY = b"1234567890abcdef12345678"
KEY = DES3.adjust_key_parity(KEY)


# ------------------ ENKRIPTIM TEKST ------------------
def enkripto_tekst():
    message = input("Shkruaj tekstin që dëshiron ta enkriptosh: ")

    cipher = DES3.new(KEY, DES3.MODE_CBC)
    iv = cipher.iv

    padded_message = pad(message.encode("utf-8"), DES3.block_size)
    encrypted_bytes = cipher.encrypt(padded_message)

    result = base64.b64encode(iv + encrypted_bytes).decode("utf-8")

    print("\nTeksti i enkriptuar (Base64):")
    print(result)


# ------------------ DEKRIPTIM TEKST ------------------
def dekripto_tekst():
    encrypted_input = input("Shkruaj tekstin e enkriptuar (Base64): ")

    try:
        data = base64.b64decode(encrypted_input)
        iv = data[:8]
        encrypted_message = data[8:]

        cipher = DES3.new(KEY, DES3.MODE_CBC, iv=iv)
        decrypted_padded = cipher.decrypt(encrypted_message)
        decrypted = unpad(decrypted_padded, DES3.block_size)

        print("\nTeksti i dekriptuar:")
        print(decrypted.decode("utf-8"))

    except:
        print("Gabim gjatë dekriptimit.")


# ------------------ ENKRIPTIM FAJLL ------------------
def enkripto_fajll():
    input_file = input("Shkruaj emrin e fajllit që dëshiron ta enkriptosh: ")

    try:
        with open(input_file, "rb") as f:
            file_data = f.read()

        cipher = DES3.new(KEY, DES3.MODE_CBC)
        iv = cipher.iv

        padded_data = pad(file_data, DES3.block_size)
        encrypted_data = cipher.encrypt(padded_data)

        output_file = "encrypted_" + input_file

        with open(output_file, "wb") as f:
            f.write(iv + encrypted_data)

        print("\nSukses!")
        print("Fajlli u enkriptua:", output_file)

    except FileNotFoundError:
        print("Gabim: Fajlli nuk u gjet.")


# ------------------ DEKRIPTIM FAJLL ------------------
def dekripto_fajll():
    input_file = input("Shkruaj emrin e fajllit të enkriptuar: ")

    try:
        with open(input_file, "rb") as f:
            data = f.read()

        iv = data[:8]
        encrypted_data = data[8:]

        cipher = DES3.new(KEY, DES3.MODE_CBC, iv=iv)
        decrypted_padded = cipher.decrypt(encrypted_data)
        decrypted_data = unpad(decrypted_padded, DES3.block_size)

        output_file = "decrypted_" + input_file.replace("encrypted_", "")

        with open(output_file, "wb") as f:
            f.write(decrypted_data)

        print("\nSukses!")
        print("Fajlli u dekriptua:", output_file)

    except FileNotFoundError:
        print("Gabim: Fajlli nuk u gjet.")
    except:
        print("Gabim gjatë dekriptimit.")


# ------------------ MENU ------------------
print("\n--- SISTEMI I ENKRIPTIMIT 3DES ---")
print("1: Enkripto Tekst")
print("2: Enkripto Fajll")
print("3: Dekripto Tekst")
print("4: Dekripto Fajll")

zgjedhja = input("Zgjidh opsionin: ")

if zgjedhja == "1":
    enkripto_tekst()
elif zgjedhja == "2":
    enkripto_fajll()
elif zgjedhja == "3":
    dekripto_tekst()
elif zgjedhja == "4":
    dekripto_fajll()
else:
    print("Opsion i pavlefshëm.")