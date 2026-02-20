import argparse
from pathlib import Path


def encryptFile(FILE, key):
        print()

def decryptFile(FILE, key):
        print()


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
    mapper




    if args.encrypt:
    #encryption process
        encryptFile(1,1)


    if args.decrypt:
        #decryption process
        decryptFile(1,1)


    

if __name__  == "__main__":
    main()

















