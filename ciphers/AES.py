'''
@ AES.py
@ Code by Xinyi Xiang
@ Advanced Encryption Scheme in python
'''

# return the AES result from given secrey key (k), plaintext(m) and cipher(x)
import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def aes():
  backend = default_backend()
  # examplary parameters
  x = "10042018000000000000000000000000"
  m = "00000000000000000000000000000000"
  k = "00000000000000000000000000000000"
  
  # compose new block ciphertext
  # for i in range(17,int(0xffffffffffffffffffffffffffffffff)+1):
  #     bc = '{:x}'.format(int(i))
  #     bc = format(i,'X')
  #     bc = bc.zfill(34-len(bc))

  cipher = Cipher(algorithms.AES(bytearray.fromhex(k)), modes.ECB(), backend=backend)
  encryptor = cipher.encryptor()
  ct = encryptor.update(bytearray.fromhex(x)) + encryptor.finalize()
  print(ct.hex())

# print the hex form of ciphertext for readability
