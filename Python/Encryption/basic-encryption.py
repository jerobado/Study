# Basic encryption using cryptography tool

from cryptography.fernet import Fernet


master_key = Fernet.generate_key()
encryption_model = Fernet(master_key)
message = 'jerobado'


def encrypt(message, model, key):

    print(f'master_key: {key}')
    encrypted_message = model.encrypt(bytes(message, 'utf-8'))
    print(f'encrypted message: {encrypted_message}')
    return encrypted_message


def decrypt(token, model):

    decrypted_message = model.decrypt(token)
    print(f'decrypted message: {decrypted_message}')
    return decrypted_message


encrypted_message = encrypt(message, encryption_model, master_key)
decrypted_message = decrypt(encrypted_message, encryption_model)

