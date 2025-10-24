import keyring
import pyperclip


# * Terminal Colors
class TerminalColors:
    RESET = "\033[0m"

    # Text styles
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    INVERSE = "\033[7m"
    HIDDEN = "\033[8m"
    STRIKE = "\033[9m"

    # Text colors
    FAILURE = "\033[31m"
    COMPLETION = "\033[32m"
    WARNING = "\033[33m"
    INFO = "\033[34m"
    DEBUG = "\033[35m"

    @staticmethod
    def colorize(text: str, *effects: str) -> str:
        return f"{''.join(effects)}{text}{TerminalColors.RESET}"


class PasswordRetriever:
    def __init__(self):
        self.name = ""
        self.attribute = ""
        self.password = ""

    def askForDetails(self):
        self.name = input("Enter name: ")
        self.attribute = input("Enter attribute: ")

    def askForPassword(self):
        self.password = input("Enter password: ")

    def setPassword(self):
        try:
            keyring.set_password(self.name, self.attribute, self.password)
            print(TerminalColors.colorize("\npassword set\n",
                                          TerminalColors.COMPLETION, TerminalColors.BOLD))
        except Exception as e:
            print(TerminalColors.colorize(f"\nError setting password: {e}\n",
                                          TerminalColors.FAILURE, TerminalColors.BOLD))

    def retrievePassword(self):
        try:
            password = keyring.get_password(self.name, self.attribute)
            if password is None:
                print(TerminalColors.colorize("\nNo password found for this service and username combination\n",
                                              TerminalColors.WARNING, TerminalColors.BOLD))
                return

            pyperclip.copy(password)
            print(TerminalColors.colorize("\npassword copied to clipboard\n",
                                          TerminalColors.COMPLETION, TerminalColors.BOLD))

        except Exception as e:
            print(TerminalColors.colorize(f"\nError retrieving password: {e}\n",
                                          TerminalColors.FAILURE, TerminalColors.BOLD))


def display_menu():
    print("-------------------"
          + TerminalColors.colorize(
              "Password Manager", TerminalColors.BOLD, TerminalColors.UNDERLINE)
          + "-------------------------")
    print("- 1. Set Password                                          -")
    print("- 2. Retrieve Password                                     -")
    print("- 3. Quit                                                  -")
    print("------------------------------------------------------------\n")


def main():
    programRun = True
    while programRun:
        display_menu()
        choice = input("Pick an option: ")
        if choice == "1":
            retriever = PasswordRetriever()
            retriever.askForDetails()
            retriever.askForPassword()
            retriever.setPassword()
        elif choice == "2":
            retriever = PasswordRetriever()
            retriever.askForDetails()
            retriever.retrievePassword()
        elif choice == "3":
            programRun = False
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
