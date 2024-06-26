"""
First success at one full round of encryption and n rounds

Next:
Iterate state by 16 chars
Rijndael Key Schedule
Cipher Block Chaining
plaintext in binary (first 4 bytes): 01110100 01100101 01110011 01110100 
key= "the more you see"
plaintext test = "testing testing9" (inside of input.txt)
"""
#74 68 65 20 6D 6F 72 65 20 79 6F 75 20 73 65 65
import numpy as np
class AES:
  def __init__(self, key):
    self.key = key
    self.AES_Sbox = (
        0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67,
        0x2B, 0xFE, 0xD7, 0xAB, 0x76, 0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59,
        0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0, 0xB7,
        0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1,
        0x71, 0xD8, 0x31, 0x15, 0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05,
        0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75, 0x09, 0x83,
        0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29,
        0xE3, 0x2F, 0x84, 0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B,
        0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF, 0xD0, 0xEF, 0xAA,
        0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C,
        0x9F, 0xA8, 0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC,
        0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2, 0xCD, 0x0C, 0x13, 0xEC,
        0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19,
        0x73, 0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE,
        0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB, 0xE0, 0x32, 0x3A, 0x0A, 0x49,
        0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
        0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4,
        0xEA, 0x65, 0x7A, 0xAE, 0x08, 0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6,
        0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A, 0x70,
        0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9,
        0x86, 0xC1, 0x1D, 0x9E, 0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E,
        0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF, 0x8C, 0xA1,
        0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0,
        0x54, 0xBB, 0x16)
    self.AES_Sbox_array = np.array(self.AES_Sbox, dtype=np.uint8).reshape((16, 16))
    self.AES_SboxInverse = (
        0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E,
        0x81, 0xF3, 0xD7, 0xFB, 0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87,
        0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB, 0x54, 0x7B, 0x94, 0x32,
        0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
        0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49,
        0x6D, 0x8B, 0xD1, 0x25, 0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16,
        0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92, 0x6C, 0x70, 0x48, 0x50,
        0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
        0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05,
        0xB8, 0xB3, 0x45, 0x06, 0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02,
        0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B, 0x3A, 0x91, 0x11, 0x41,
        0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
        0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8,
        0x1C, 0x75, 0xDF, 0x6E, 0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89,
        0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B, 0xFC, 0x56, 0x3E, 0x4B,
        0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
        0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59,
        0x27, 0x80, 0xEC, 0x5F, 0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D,
        0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF, 0xA0, 0xE0, 0x3B, 0x4D,
        0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
        0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63,
        0x55, 0x21, 0x0C, 0x7D)
    self.AES_SboxInverse_array = np.array(self.AES_SboxInverse, dtype=np.uint8).reshape(
      (16, 16))
    self.AES_Encrypt()
  

  #Xors two binary string
  def xor(self, byte1, byte2):
    result = []
    for bit1, bit2 in zip(byte1, byte2):
      if bit1 == bit2:
        result.append("0")
      else:
        result.append("1")
    #print(byte1 + "   " + byte2+"  =  "+str(result))
    return ''.join(result)
  
  
  
  
  
  #Char to binary
  def toBinary(self, a):
    binary_list = []
    for char in a:
      binary_char = format(ord(char), '08b')
      binary_list.append(binary_char)
    return binary_list
  
  
  #Hex to binary
  def hex_to_binary(self, hex_string):
    decimal_number = int(hex_string, 16)
    binary_string = bin(decimal_number)[2:].zfill(8)
    return (binary_string)
  
  
  def addRoundKey(self, state, keyBytesArr):
    for col in range(4):
      for row in range(4):
        temp = self.xor(state[col, row], keyBytesArr[col, row])
        self.state[col, row] = temp
  
  #given input byte in binary switch and return as uint8
  def SBox_Lookup(self, byte):
    b11 = byte[:4]
    b12 = byte[4:]
    column = int(b11, 2)
    row = int(b12, 2)
    return (self.AES_Sbox_array[column, row])
  

  def substituteArray(self, state):
    for col in range(4):
      for row in range(4):
        self.state[col, row] = (self.SBox_Lookup(state[col, row]))
  
  
  def shiftRows(self, state):
    state[:, 1] = [state[1, 1], state[2, 1], state[3, 1], state[0, 1]]
    # Shift the third column two positions down
    state[:, 2] = [state[2, 2], state[3, 2], state[0, 2], state[1, 2]]
    # Shift the fourth column three positions down
    state[:, 3] = [state[3, 3], state[0, 3], state[1, 3], state[2, 3]]
    return state
  




  

  def gmul(self, a, b):
    if b == 1:
        return a
    tmp = (a << 1) & 0xff
    if b == 2:
        return tmp if a < 128 else tmp ^ 0x1b
    if b == 3:
        return self.gmul(a, 2) ^ a
    
  def mixSingleColumn(self, col):
    a=int(col[0])
    b=int(col[1])
    c=int(col[2])
    d=int(col[3])
    col[0] = (self.gmul(a, 2) ^ self.gmul(b, 3) ^ self.gmul(c, 1) ^ self.gmul(d, 1))
    col[1] = (self.gmul(a, 1) ^ self.gmul(b, 2) ^ self.gmul(c, 3) ^ self.gmul(d, 1))
    col[2] = (self.gmul(a, 1) ^ self.gmul(b, 1) ^ self.gmul(c, 2) ^ self.gmul(d, 3))
    col[3] = (self.gmul(a, 3) ^ self.gmul(b, 1) ^ self.gmul(c, 1) ^ self.gmul(d, 2))
    return col

  def mixColumns(self, state):
      # Create an empty array to store the result
        result = np.empty_like(state, dtype=np.uint8)
        
        # Apply mixSingleColumn operation to each column separately
        for col_idx in range(4):
            column = state[col_idx,:]  # Extract the column
            mixed_column = self.mixSingleColumn(column)  # Apply mixSingleColumn function
            result[:, col_idx] = mixed_column  # Store the result back into the result array
        
        return(result)




    


    
  
  def AES_Encrypt(self):
    #Read file
    rounds=1
    input = "input.txt"
    with open(input, "r") as file:
      #Read first 16 chars
      data = self.toBinary(file.read()[:16])
  
    # Grab first 128 bits of the ciphertext and the entire key and condense to a 4x4 array of bytes for both
    self.state = np.array(list(data)).reshape(4, 4).T
    self.keyBytes = [key[i:i + 8] for i in range(0, len(key), 8)]
    self.keyBytesArr = np.array(self.keyBytes).reshape(4, 4)

    while rounds <=10:
      print("\nStarting text for round "+str(rounds)+":")
      for row in range(4):
        print(self.state[0, row] + " " + self.state[1, row] + " " + self.state[2, row] + " " +
              self.state[3, row] + " ")
      print("\n")

      print("\nKey "+str(rounds)+" in Binary:")
      for row in range(4):
        print(self.keyBytesArr[0, row] + " " + self.keyBytesArr[1, row] + " " +
              self.keyBytesArr[2, row] + " " + self.keyBytesArr[3, row] + " ")
        
        
      #RoundKey
      self.addRoundKey(self.state, self.keyBytesArr)
      print("\nCiphertext After Round Key:")
      for row in range(4):
        print(self.state[0, row] + " " + self.state[1, row] + " " + self.state[2, row] + " " +
              self.state[3, row] + " ")
      print("\n")
    
      #Substiute
      self.substituteArray(self.state)
      print("\nCiphertext After Substitution:")
      for row in range(4):
        print(self.state[0, row] + " " + self.state[1, row] + " " + self.state[2, row] + " " +
              self.state[3, row] + " ")
      print("\n")
    
      #Shift Rows
      self.state = self.shiftRows(self.state)
      print("\nCiphertext After Shift Rows: (INTEGER)")
      for row in range(4):
        print(self.state[0, row] + " " + self.state[1, row] + " " + self.state[2, row] + " " +
              self.state[3, row] + " ")



      #Shift Mix Columns
      self.state = (self.mixColumns(self.state))
      print("\nCiphertext After Mix Columns: (HEX)")
      
      for row in range(4):
        print(hex(self.state[0, row])[2:].zfill(2) + " " +
                hex(self.state[1, row])[2:].zfill(2) + " " +
                hex(self.state[2, row])[2:].zfill(2) + " " +
                hex(self.state[3, row])[2:].zfill(2))
        

      binary_string = ''.join([format(num, '08b') for num in self.state.flatten()])
      self.bin = [binary_string[i:i + 8] for i in range(0, len(binary_string), 8)]
      self.state = np.array(self.bin).reshape(4, 4)

      print("\n")
      rounds+=1
    print("\n\nFINAL OUTPUT AFTER 10 ROUNDS:\n")
    result = ""
    for row in range(4):
        # Print in order left to right
        result += ''.join(hex(self.state[row, 0]),
                          hex(self.state[row, 1]),
                          hex(self.state[row, 2]),
                          hex(self.state[row, 3]))
    print(result)
    


    
   
  
#Run
key = "01110100011010000110010100100000011011010110111101110010011001010010000001111001011011110111010100100000011100110110010101100101"
aes = AES(key)

print("\n")




"""result = ""
    for row in range(4):
        # Print in order left to right
        result += ''.join([hex(self.state[row, 0])[2:].zfill(2),
                          hex(self.state[row, 1])[2:].zfill(2),
                          hex(self.state[row, 2])[2:].zfill(2),
                          hex(self.state[row, 3])[2:].zfill(2)])
    print(result)"""

"""def printHex(val):
    return print('{:02x}'.format(val), end=' ')"""
