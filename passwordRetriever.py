import keyring
import tkinter as tk


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


# * Functions


def setPassword(name, attr, psw):
    try:
        keyring.set_password(name, attr, psw)
        print(TerminalColors.colorize("\npassword set\n",
                                      TerminalColors.COMPLETION, TerminalColors.BOLD))
    except Exception as e:
        print(TerminalColors.colorize(f"\nError setting password: {e}\n",
              TerminalColors.FAILURE, TerminalColors.BOLD))


def retrievePassword(name, attr):
    try:
        password = keyring.get_password(name, attr)
        print(TerminalColors.colorize("\npassword copied\n",
                                      TerminalColors.COMPLETION, TerminalColors.BOLD))
        r = tk.Tk()
        r.withdraw()  # hide main window
        r.clipboard_clear()
        r.clipboard_append(password)
        r.update()  # keep clipboard content after closing
        r.destroy()

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
            name = input("Enter name: ")
            attribute = input("Enter attribute: ")
            password = input("Enter password: ")
            setPassword(name, attribute, password)
        elif choice == "2":
            name = input("Enter name: ")
            attribute = input("Enter attribute: ")
            retrievePassword(name, attribute)
        elif choice == "3":
            programRun = False
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
