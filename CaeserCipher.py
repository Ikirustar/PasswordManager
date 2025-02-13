# functions
def encrypt(ms, s):
    psList = list(ms)
    encryptedMessage = ""
    for i in range(len(psList)):
        if psList[i] in alphabet:
            if psList[i].islower():
                encryptedMessage += alphabet[(
                    alphabet.index(psList[i]) + int(s)) % 26]
            else:
                encryptedMessage += alphabet[(alphabet.index(
                    psList[i].lower()) + int(s)) % 26].upper()
        else:
            encryptedMessage += psList[i]

    return encryptedMessage


def decrypt(ms, k):
    msList = list(ms)
    decryptedMessage = ""
    for i in range(len(msList)):
        if msList[i] in alphabet:
            if msList[i].islower():
                decryptedMessage += alphabet[(
                    alphabet.index(msList[i]) - int(k)) % 26]
            else:
                decryptedMessage += alphabet[(alphabet.index(
                    msList[i].lower()) - int(k)) % 26].upper()
        else:
            decryptedMessage += msList[i]

    return decryptedMessage


# variables
alphabet = [chr(i) for i in range(97, 123)]
message = []

# menu selection
programRun = True
while programRun:

    print("------------------------ CipherTask ------------------------")
    print("- 1. Encrypt                                               -")
    print("- 2. Decrypt                                               -")
    print("- 3. Quit                                                  -")
    print("------------------------------------------------------------\n")

    choice = input("Pick an option: ")
    if choice == "1":
        message = input("Enter message: ")
        shift = input("Enter number of letters to shift: ")
        print("\nEncrypted message: ", encrypt(message, shift))
        programRun = False
    elif choice == "2":
        message = input("Enter message: ")
        key = input("Enter key: ")
        print("\nDecrypted message: ", decrypt(message, key))
