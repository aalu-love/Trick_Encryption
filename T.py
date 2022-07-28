# import the necessary packages
import argparse
import random
from cryptography.fernet import Fernet

class Encryptor():

    def key_create(self,k):
        key = Fernet.generate_key()
        return key

    def key_write(self, key, key_name):
        with open(key_name, 'wb') as mykey:
            mykey.write(key)

    def key_load(self, key_name):
        with open(key_name, 'rb') as mykey:
            key = mykey.read()
        return key


    def file_encrypt(self, key, original_file, encrypted_file):
        
        f = Fernet(key)

        with open(original_file, 'rb') as file:
            original = file.read()

        encrypted = f.encrypt(original)

        with open (encrypted_file, 'wb') as file:
            file.write(encrypted)

    def file_decrypt(self, key, encrypted_file, decrypted_file):
        
        f = Fernet(key)

        with open(encrypted_file, 'rb') as file:
            encrypted = file.read()

        decrypted = f.decrypt(encrypted)

        with open(decrypted_file, 'wb') as file:
            file.write(decrypted)

            return decrypted

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

encryptor = Encryptor()
k = ''
code = random.randint(000,999)
byte = code.to_bytes(2,'big')
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser(description="Usage: 1.Genrate_Key 2.Encryprt 3.Decryprt")
#ap.add_argument("-n", "--name", required=False, help="name of the user")
#ap.add_argument("-j", "--num", required=False, help="Enter number")
ap.add_argument("-k", "--key", required=False, help="Genrate Key 'True T or False F'")
ap.add_argument("-n", "--name", required=False, help="Key Name : -n key.dat or --name key.dat (default: key.data)")
ap.add_argument("-en", "--encrypt", required=False, help="Encrypt File : -en 'FileName'")
ap.add_argument("-de", "--decrypt", required=False, help="Decrypt File : -de 'FileName'")
ap.add_argument("-load", "--loadkey", required=False, help="Load key : -load 'FileName'")
ap.add_argument("-key", "--cryptkey", required=False, help="Decrypt File : -key 'Filename'")
ap.add_argument("-t", "--tym", required=False, help="Decrypt Time : -t 'number'")
args = vars(ap.parse_args())

# display a friendly message to the user
#print("Hi there {}, it's nice to meet you! Here is your number {}:".format(args["name"],args["num"]))



if args['key'] == "T":
    k = encryptor.key_create(args['key'])
    if args['name'] != None: 
        encryptor.key_write(k+byte,args['name'])
    else:
        encryptor.key_write(k+byte,'key.k')
    l = k+byte
    d = sum_digits(l[-1])
    print(d)

    
elif args['encrypt'] != None and args['cryptkey'] != None:
    loaded_key=encryptor.key_load(args['cryptkey'])
    name = args['encrypt']
    print(loaded_key)
    multiple = sum_digits(loaded_key[-1])
    print(multiple)
    for x in range(multiple):
        encryptor.file_encrypt(loaded_key, name, name)


elif args['decrypt'] != None and args['cryptkey'] != None:
    loaded_key=encryptor.key_load(args['cryptkey'])
    name = args['decrypt']
    times = args['tym']
    for x in range(int(times)):
        encryptor.file_decrypt(loaded_key, name, name)


elif args['loadkey'] != None:
    l = encryptor.key_load(args['loadkey'])
    print(l[-1])
