from Crypto import Random
from Crypto.Cipher import AES
import base64, hashlib

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-s[-1]]

class AESCipher:
    def __init__(self, key):
        self.key = hashlib.sha256(key.encode("utf-8")).digest()

    def encrypt(self, raw):
        raw = pad(raw)
        IV = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, IV)
        return base64.b64encode(IV + cipher.encrypt(raw.encode("utf8")))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        IV = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, IV)
        return unpad(cipher.decrypt(enc[16:]))

