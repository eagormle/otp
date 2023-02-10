#Ethanb Gormley
#Pad cipher using user input for CIT 55510
#program was written in C# iniially since I write in it at work
#but i do not have .net installed on this mac and I do not
#feel like configuring it

#import random and string so it can generate readable characters
import random
import string

#generate the key according to how big the plaintext is
def generate_key(plaintext):
    key = ''.join(random.choices(string.ascii_uppercase, k=len(plaintext)))
    return key

#encrypt the text using the user provided text and generated key
def encrypt(plaintext, key):
    ciphertext = ""
    for i, char in enumerate(plaintext):
        ciphertext += chr((ord(char) + ord(key[i % len(key)])) % 26 + 65)
    return ciphertext

#decrypt everthing by doing what i basically did backwards
def decrypt(ciphertext, key):
    plaintext = ""
    for i, char in enumerate(ciphertext):
        plaintext += chr((ord(char) - ord(key[i % len(key)])) % 26 + 65)
    return plaintext

#the heart of the program
plaintext = input("Enter plaintext: ")
plaintext = plaintext.upper()
key = generate_key(plaintext)
ciphertext = encrypt(plaintext, key)

#the soul
print("Plaintext: ", plaintext)
print("Key: ", key)
print("Ciphertext: ", ciphertext)
print("Decrypted Text: ", decrypt(ciphertext, key))


    #upload to github and put link on pdf for refrence
    #git broken
