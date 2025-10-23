import keyring

# Set password
keyring.set_password("personalTest", "password", "test")

# Retrieve it later
password = keyring.get_password("personalTest", "password")

print(password)  # securely retrieved from system store
