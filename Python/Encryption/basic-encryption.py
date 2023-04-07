# Basic encryption using cryptography library

from cryptography.fernet import Fernet


master_key = Fernet.generate_key()
encryption_model = Fernet(master_key)
message = 'jerobado'


def encrypt(message, model):

    return model.encrypt(bytes(message, 'utf-8'))


def decrypt(token, model):

    return model.decrypt(token)
    

# Perform encryption and decryption
encrypted_message = encrypt(message, encryption_model)
decrypted_message = decrypt(encrypted_message, encryption_model)

# Display output
print(f'master_key: {master_key}')
print(f'encrypted message: {encrypted_message}')
print(f'decrypted message: {decrypted_message}')