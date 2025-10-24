import customtkinter
from passwordRetriever import PasswordRetriever


# * Password Retriever
retriever = PasswordRetriever()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # * Main Application Window *#

        customtkinter.set_appearance_mode("dark")  # default
        self.geometry("550x300")
        self.title("Password Retriever")

        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

    def loadWidgets(self):

        # * Widgets *#

        # Name input
        self.namelabel = customtkinter.CTkLabel(
            self, text="Name:", width=100, font=("sans serif", 20))
        self.namelabel.grid(row=1, column=1, sticky="", padx=0, pady=0)

        self.nameEntry = customtkinter.CTkEntry(self, width=100)
        self.nameEntry.grid(row=1, column=1, sticky="s", padx=0, pady=0)

        # Attribute input
        self.attributelabel = customtkinter.CTkLabel(
            self, text="Attribute", width=100, font=("sans serif", 20))
        self.attributelabel.grid(
            row=1, column=2, sticky="", padx=0, pady=0)

        self.attributeEntry = customtkinter.CTkEntry(self, width=100)
        self.attributeEntry.grid(row=1, column=2, sticky="s", padx=0, pady=0)

        # Set password button
        self.setPasswordButton = customtkinter.CTkButton(
            self, text="Set Password", width=130, height=40, fg_color="#1f6aa5", hover_color="#367fa9", font=("sans serif", 14), corner_radius=15, command=self.setPasswordDialog)
        self.setPasswordButton.grid(row=2, column=4, sticky="", padx=0, pady=0)

        # Get password button
        self.getPasswordButton = customtkinter.CTkButton(
            self, text="Get Password", width=130, height=40, fg_color="#1f6aa5", hover_color="#367fa9", font=("sans serif", 14), corner_radius=15, command=self.getPasswordProcess)
        self.getPasswordButton.grid(row=1, column=4, sticky="", padx=0, pady=0)

        # Password action label
        self.passwordActionLabel = customtkinter.CTkLabel(
            self, text="", text_color="green", width=1, font=("sans serif", 20))
        self.passwordActionLabel.grid(
            row=3, column=2, padx=0, pady=0, sticky="news")

    def setPasswordDialog(self):
        retriever.password = customtkinter.CTkInputDialog(
            text="Enter Password:", title="Password Input").get_input()
        if retriever.password:
            retriever.name = self.nameEntry.get()
            retriever.attribute = self.attributeEntry.get()
            retriever.setPassword()
            self.passwordActionLabel.configure(
                text="Password set", text_color="green")

        else:
            self.passwordActionLabel.configure(
                text="No password entered", text_color="yellow")
            return

    def getPasswordProcess(self):
        retriever.name = self.nameEntry.get()
        retriever.attribute = self.attributeEntry.get()

        if not retriever.name or not retriever.attribute:
            self.passwordActionLabel.configure(
                text="Enter name and attribute", text_color="yellow")
            return

        retriever.retrievePassword()
        self.passwordActionLabel.configure(
            text="Password copied", text_color="green")


def main():
    app = App()
    app.loadWidgets()
    app.mainloop()


if __name__ == "__main__":
    main()
