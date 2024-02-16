from Crypto.Cipher import AES
import binascii

class AESCipher:
    def __init__(self):
        self.key = b"1wOS377woe39ksf/"
        self.iv = b"qawsedploeSD(234"
        # self.key = b"oW1mY2vHAXbiBQtL"
        # self.iv = b"CmYUOq8cIpyr1H6p"
        
    def aes_decrypt(self, input_bytes):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        decrypted = cipher.decrypt(input_bytes)
        return decrypted.decode().rstrip('\0')

    def aes_encrypt(self, input_text):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        padded_text = self.pad_text(input_text)
        encrypted = cipher.encrypt(padded_text.encode())
        return encrypted

    def pad_text(self, text):
        block_size = 16
        padding = block_size - (len(text) % block_size)
        return text + chr(padding) * padding

    def byte_array_to_hex_string(self, byte_array):
        return binascii.hexlify(byte_array).decode()

    def encrypt(self, text):
        return self.byte_array_to_hex_string(self.aes_encrypt(text)).upper()

    def decrypt(self, text_hex):
        return self.aes_decrypt(bytes.fromhex(text_hex))