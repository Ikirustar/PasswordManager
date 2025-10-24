import keyring

# Set password
keyring.set_password("chris", "pass", "12345")

# Retrieve it later
password = keyring.get_password("chris", "pass")

print(password)  # securely retrieved from system store
