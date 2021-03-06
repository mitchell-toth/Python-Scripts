#2-rail encryption

def twoRailEncryption(plainText):
    odds=""
    evens=""
    for i in range(0,len(plainText),2):
        evens += plainText[i]
    for i in range(1,len(plainText),2):
        odds += plainText[i]
    return odds + evens

def twoRailDecryption(cipherText):
    halfLength = len(cipherText)//2
    oddChars = cipherText[:halfLength]
    evenChars = cipherText[halfLength:]
    plainText=""
    for i in range(halfLength):
        plainText += evenChars[i] + oddChars[i]
    if len(oddChars) < len(evenChars):
        plainText += evenChars[-1]
    return plainText

print(twoRailEncryption("Encrypted message..."))
print(twoRailDecryption(twoRailEncryption("Encrypted message...")))



def stripSpaces(myString):
    strippedString = ""
    for ch in myString:
        if ch != " ":
            strippedString += ch
    return strippedString

print(stripSpaces("This is a test"))
