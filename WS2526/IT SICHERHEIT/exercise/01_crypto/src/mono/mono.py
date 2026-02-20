import argparse
from pathlib import Path


def cleanFile(fileText:str):         
    text = fileText
    text = text.lower()
    return text

def replaceLetters(key, text):
    resultText = ""
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    for char in text:
        if char.isalpha():
            index = ALPHABET.find(char)
            resultText += key[index]
    return resultText
def reverseReplacement(key, text):
    resultText = ""
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    for char in text:
        if char.isalpha():
            index = key.find(char)
            print(index)
            resultText += ALPHABET[index]
    return resultText






def encryptFile(FILE, key, outfile = "abdullah.txt"):
    FILE1 = Path(FILE)
    plaintext = Path.read_text(FILE1)
    plaintext = cleanFile(plaintext)
    plaintext = replaceLetters(key,plaintext)
    outputPath = Path(outfile)
    outputPath.write_text(plaintext)



def decryptFile(FILE, key, outfile = "jumbo.txt"):
    FILE1 = Path(FILE)
    ciphertext = FILE1.read_text()
    ciphertext = reverseReplacement(key, ciphertext)
    outputFile = Path(outfile)
    outputFile.write_text(ciphertext)
    


def main():  

    parser = argparse.ArgumentParser()

    #mutually exclusive group for encrypt XOR decrypt within parser
    encr_decr = parser.add_mutually_exclusive_group()
    encr_decr.add_argument("--encrypt", help= "give key nigga")
    encr_decr.add_argument("--decrypt", help= "give key nigga")


    parser.add_argument("--out" , help = 'Outfile where')
    parser.add_argument("FILE")
    args = parser.parse_args()







    FILE = Path(args.FILE)
    FILE_CONTENTS = Path.read_text(FILE)

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    




    if args.encrypt:
    #encryption process
        encryptFile(args.FILE , args.encrypt)


    if args.decrypt:
        #decryption process
        decryptFile(args.FILE, args.decrypt)


main()

















