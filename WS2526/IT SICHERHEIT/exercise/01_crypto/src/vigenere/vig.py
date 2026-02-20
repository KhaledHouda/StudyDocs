import argparse
from pathlib import Path

def offsetAlphabet(offset):
    currentalphabet = ""
    DEFAULT_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    for i in range(offset, len(DEFAULT_ALPHABET) ):
        currentalphabet += DEFAULT_ALPHABET[i]
    for i in range(0, offset):
        currentalphabet += DEFAULT_ALPHABET[i]
    return currentalphabet

def cleanFile(fileText:str):         
    text = fileText
    text = text.lower()
    temp = ""
    for letter in text:
        if letter.isalpha():
            temp += letter

    text = temp 
    return text
def replaceLetters(key, text):
    offset = 0
    
    resultText = ""
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    workingAlphabet = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    for char in text:
        positionOfKey = count % len(key)
        offset = ALPHABET.find(key[positionOfKey])
        workingAlphabet = offsetAlphabet(offset)
        resultText += workingAlphabet[ALPHABET.find(char)]
        count +=1
    return resultText
def reverseReplacement(key, text):
    offset = 0
    
    resultText = ""
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    workingAlphabet = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    for char in text:
        positionOfKey = count % len(key)
        offset = ALPHABET.find(key[positionOfKey])
        workingAlphabet = offsetAlphabet(offset)
        resultText += ALPHABET[workingAlphabet.find(char)]
        count +=1
    return resultText


def vigEncrypter(key, PATH, outfile = "locked.txt"):
    text = Path(PATH)
    text = text.read_text()
    text = cleanFile(text)
    text = replaceLetters(key, text)
    outfile = Path(outfile)
    outfile.write_text(text)



def vigDecrypter(key, PATH, outfile = "unlocked.txt"):
    text = Path(PATH)
    text = text.read_text()
    text = cleanFile(text)
    text = reverseReplacement(key, text)
    outfile = Path("locked.txt")
    outfile.write_text(text)
    


    



def main():
  

    parser = argparse.ArgumentParser()

    #mutually exclusive group for encrypt XOR decrypt within parser
    encr_decr = parser.add_mutually_exclusive_group()
    encr_decr.add_argument("--encrypt", help= "give key nigga")
    encr_decr.add_argument("--decrypt", help= "give key nigga")


    parser.add_argument("--out" , help = 'Outfile where')
    parser.add_argument("FILE")
    args = parser.parse_args()

    if args.encrypt:
        vigEncrypter(args.encrypt , args.FILE)
    if args.decrypt:
        vigDecrypter(args.decrypt, args.FILE)
    






















main()