#!/bin/python3


# encrypt rotate
def encrypt_rotate(key_intArr, data_intArr):

    for i in range(0, len(data_intArr)):
        key_loc = i%len(key_intArr)
        data_intArr[i] = (data_intArr[i] + key_intArr[key_loc])%256

# encrypt swap
def encrypt_swap(key_intArr, data_intArr):

    for i in range(0, len(data_intArr)):
        key_loc = i%len(key_intArr)
        data_loc = (i+key_intArr[key_loc])%len(data_intArr)
        
        swapBuff = data_intArr[i]
        data_intArr[i] = data_intArr[data_loc]
        data_intArr[data_loc] = swapBuff

# decrypt swap
def decrypt_swap(key_intArr, data_intArr):

    for i in range(len(data_intArr)-1, 0-1, -1):
        key_loc = i%len(key_intArr)
        data_loc = (i+key_intArr[key_loc])%len(data_intArr)
        
        swapBuff = data_intArr[data_loc]
        data_intArr[data_loc] = data_intArr[i]
        data_intArr[i] = swapBuff

# decrypt rotate
def decrypt_rotate(key_intArr, data_intArr):

    for i in range(0, len(data_intArr)):
        key_loc = i%len(key_intArr)
        data_intArr[i] = (data_intArr[i] - key_intArr[key_loc])%256



# allows each character to have an impact
# encrypt byte by byte
def encrypt_byte_by_byte(key_intArr, data_intArr):
    for j in range(0, len(key_intArr)):
        for i in range(0, len(data_intArr)):
            
            # rotate
            data_intArr[i] = (data_intArr[i] + key_intArr[j]*i)%256
            
        for i in range(0, len(data_intArr)):
        
            # swap
            data_loc = (i+key_intArr[j]*i)%len(data_intArr)
            
            swapBuff = data_intArr[i]
            data_intArr[i] = data_intArr[data_loc]
            data_intArr[data_loc] = swapBuff

# decrypt byte by byte
def decrypt_byte_by_byte(key_intArr, data_intArr):
    for j in range(len(key_intArr)-1, 0-1, -1):
        for i in range(len(data_intArr)-1, 0-1, -1):
        
            # swap
            data_loc = (i+key_intArr[j]*i)%len(data_intArr)
            
            swapBuff = data_intArr[data_loc]
            data_intArr[data_loc] = data_intArr[i]
            data_intArr[i] = swapBuff
            
        for i in range(len(data_intArr)-1, 0-1, -1):
            
            # rotate
            data_intArr[i] = (data_intArr[i] - key_intArr[j]*i)%256

