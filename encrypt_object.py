#!/bin/python3
import sys
import random
from encrypt_decrypt import *

args = sys.argv

def print_info():
    print("")
    print("Encrypt object:")
    print("encrypt_object.py e [passphrase] [size_of_key] [object]")
    print("")
    print("Example:")
    print("encrypt_object.py e \"good@forgetting\" 4096 data.txt")
    print("output: key_material.js and data.js")
    print("")
    print("Convert int array to bin:")
    print("encrypt_object.py c [object]")
    exit()

if len(args) < 3:
    print_info()

if args[1] == 'c':
    if len(args) != 3:
        print_info()
    
    try:
        with open(args[2], 'rb') as file:
            data_raw = file.read()
        pass
    except FileNotFoundError:
        print("File not found")
        exit()

    output_file = args[2].rsplit(".", 1)[0] + ".bin"
    
    bin_output=b''
    for i in range(0, len(data_raw)//3):
        hex_string = chr(data_raw[i*3]) + chr(data_raw[i*3+1])
        bin_output += bytes([int(hex_string, 16)])
    
    with open(output_file, 'wb') as file:
        file.write(bin_output)
    exit()
    
if len(args) < 5:
    print_info()

if args[1] == 'e':
    if len(args) != 5:
        print_info()
    
    try:
        with open(args[4], 'rb') as file:
            data_raw = file.read()
        pass
    except FileNotFoundError:
        print("File not found")
        exit()

    passphrase = args[2]
    key_size = args[3]
    #output_file = args[4].rsplit(".", 1)[0] + ".js"
    
    # convert each character into an integer
    passphrase_intArr=[]
    for ch in passphrase:
        passphrase_intArr.append(ord(ch))
        
    data_intArr=[]
    for ch in data_raw:
        data_intArr.append(ch)
    
    # generate key
    key_intArr = []
    random_val = 0
    key_val = 0
    for i in range(0, int(key_size)):
        while random_val == 0 or random_val == key_val: 
            random_val = random.randint(0, 255)
        key_val = random_val
        key_intArr.append(key_val)
    
    # encrypt data
    encrypt_rotate(key_intArr, data_intArr)
    encrypt_swap(key_intArr, data_intArr)
    
    # create the key material
    keyMat_intArr = key_intArr
    encrypt_byte_by_byte(passphrase_intArr, keyMat_intArr)
    
    # output data to js file
    data_jsVar="var data = ["
    for d in data_intArr:
        data_jsVar += "0x%x, " % (d)
    data_jsVar += "];"
    
    with open("data.js", 'w') as file:
        file.write(data_jsVar)

    # output key material to js file
    key_material_jsVar="var key_material = ["
    for d in keyMat_intArr:
        key_material_jsVar += "0x%x, " % (d)
    key_material_jsVar += "];"
    
    with open("key_material.js", 'w') as file:
        file.write(key_material_jsVar)

