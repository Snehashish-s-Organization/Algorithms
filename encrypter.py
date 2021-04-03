# Made by Ishan Kashyap
# Made on 03-04-2021
# Developer contact: ishan.kashyap@sahyadrischool.org
# This is a string encrypter i have made and basically it encrypts the string
import string

letters = string.ascii_letters

def encrypt(text, key):
    # This function impliments the ceaser encrytion by encrypting the text
    # There are two parameters to be passed
    # 1) The string you want to encrypt
    # 2) by how much do you want to encrypt

    # making a variable to store cyphered text
    encrypted_text = ""

    # runnin a for loop through each element in text
    for i in text:
        # if its a letter shift its value
        try:
            # geting index of i, shifting it, geting its mod 26, then finding
            # corresponding value and concatenating it to encrypted text
            encrypted_text += letters[(letters.index(i) + key) % len(letters)]
        # other vise not cipheroing it
        except ValueError:
            encrypted_text += i
    # finally, returning ciphered text
    return encrypted_text


def decrypt(text, key):
    # This function decrypts the string
    # There are two parameters to be passed
    # 1) The string you want to decrypt
    # 2) what is the level of encryption

    # Creating a variable to store the decrypted string
    decrypted_text = ""

    # runnin a for loop through each element in text
    for i in text:

        # if its a letter shifting its value
        try:
            # get index of i, shift it, get its mod 26, then finding
            # corresponding value and concatenating it to encrypted text
            decrypted_text += letters[letters.index(i) - key % len(letters)]

        # other vise not cipheroing it
        except ValueError:
            decrypted_text += i
    # finally, returning ciphered text
    return decrypted_text
