import argparse
parser = argparse.ArgumentParser()

#mutually exclusive group for encrypt XOR decrypt within parser
encr_decr = parser.add_mutually_exclusive_group()
encr_decr.add_argument("--encrypt", help= "give key nigga")
encr_decr.add_argument("--decrypt", help= "give key nigga")


parser.add_argument("--out" , help = 'Outfile where')
parser.add_argument("FILE")
args = parser.parse_args()







FILE = args.FILE


if args.encrypt:
    #encryption process
    encrypt()


if args.decrypt:
    #decryption process
    decrypt()




def encrypt(FILE, key):
    

def decrypt(FILE, key):



    



















