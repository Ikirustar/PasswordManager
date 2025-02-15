# Constants

ALPHABET = [chr(i) for i in range(97, 123)]
# Functions


def encrypt(ms, s):
    psList = list(ms)
    encryptedMessage = ""
    for i in range(len(psList)):
        if psList[i] in ALPHABET:
            if psList[i].islower():
                encryptedMessage += ALPHABET[(
                    ALPHABET.index(psList[i]) + int(s)) % 26]
            else:
                encryptedMessage += ALPHABET[(ALPHABET.index(
                    psList[i].lower()) + int(s)) % 26].upper()
        else:
            encryptedMessage += psList[i]

    return encryptedMessage


def decrypt(ms, k):
    msList = list(ms)
    decryptedMessage = ""
    for i in range(len(msList)):
        if msList[i] in ALPHABET:
            if msList[i].islower():
                decryptedMessage += ALPHABET[(
                    ALPHABET.index(msList[i]) - int(k)) % 26]
            else:
                decryptedMessage += ALPHABET[(ALPHABET.index(
                    msList[i].lower()) - int(k)) % 26].upper()
        else:
            decryptedMessage += msList[i]

    return decryptedMessage


def display_menu():
    print("------------------------ CipherTask ------------------------")
    print("- 1. Encrypt                                               -")
    print("- 2. Decrypt                                               -")
    print("- 3. Quit                                                  -")
    print("------------------------------------------------------------\n")


def main():
    programRun = True
    while programRun:
        display_menu()
        choice = input("Pick an option: ")
        if choice == "1":
            message = input("Enter message: ")
            shift = input("Enter number of letters to shift: ")
            if shift.isdigit():
                print("\nEncrypted message: ", encrypt(message, shift))
            else:
                print("Invalid input. Please enter a valid number for the shift.")
        elif choice == "2":
            message = input("Enter message: ")
            key = input("Enter key: ")
            if key.isdigit():
                print("\nDecrypted message: ", decrypt(message, key))
            else:
                print("Invalid input. Please enter a valid number for the key.")
        elif choice == "3":
            programRun = False
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
