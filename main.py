from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import base64

KEY = b"1234567890abcdef12345678"
KEY = DES3.adjust_key_parity(KEY)
