"""
Needed:
bitwise XOR done
subsitution table i.p.
purmutation
key Rijndael key schedule
Implementation of rounds and ending on an XOR
Adaptability for 192 and 256 bit key encryption
Output to text
Condensed to hexidecimal
Make it faster
Organize it all / condense into fewer functions and one loop for n rounds depending on 128,192,256
plaintext in binary (first 4 bytes): 01110100 01100101 01110011 01110100 

key= "the more you see" 16 chars / bytes 128 bits
01110100 01101000 01100101 00100000 01101101 01101111 01110010 01100101 00100000 01111001 01101111 01110101 00100000 01110011 01100101 01100101
"""
#74 68 65 20 6D 6F 72 65 20 79 6F 75 20 73 65 65
import numpy as np
import math

key = "01110100011010000110010100100000011011010110111101110010011001010010000001111001011011110111010100100000011100110110010101100101"


def bitWiseXOR(plaintext,key):
    ciphertext = []
    for i in range(len(plaintext)):
        if plaintext[i] == key[i]:
            ciphertext.append("0")
        else:
            ciphertext.append("1")
    return ''.join(ciphertext)


def toBinary(a):
  binary_list = []
  for char in a:
      binary_char = format(ord(char), '08b')
      binary_list.append(binary_char)
  return binary_list


def toHex(a):
  print("N/A")

input = "input.txt"
with open(input, "r") as file:
    #Read first 16 chars
    data = toBinary(file.read()[:16])


# Grab first 128 bits of the ciphertext and the entire key and condense to a 4x4 array of bytes for both
ptBinaryArr = np.array(list(data)).reshape(4,4).T
keyBytes = [key[i:i+8] for i in range(0, len(key), 8)]
keyBytesArr = np.array(keyBytes).reshape(4, 4).T


print("\nPlaintext in Binary:")
for col in range(1):
  print("Column", col+1, ":")
  for row in range(4):
    print(ptBinaryArr[row, col])

print("\nKey in Binary:")
for col in range(1):
  print("Column", col+1, ":")
  for row in range(4):
    print(keyBytesArr[row, col])

print("\nCiphertext after XOR in Binary XOR 1 Round 1:")
for col in range(1):
  print("Column", col+1, ":")
  for row in range(4):
    print(bitWiseXOR(keyBytesArr[row, col],ptBinaryArr[row,col]))
