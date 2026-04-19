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