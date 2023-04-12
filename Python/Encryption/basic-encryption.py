# Basic encryption using cryptography library

from cryptography.fernet import Fernet


def generate_private_key() -> str:

    return str(Fernet.generate_key(), 'utf-8')


def create_fernet_model(key : bytes | str) -> Fernet:

    return Fernet(key)


def encrypt(plaintext: str, model: Fernet) -> str:

    encoding = 'utf-8'
    result = model.encrypt(bytes(plaintext, encoding))
    
    return str(result, encoding)


def decrypt(ciphertext: str, model: Fernet) -> str:

    return str(model.decrypt(ciphertext), 'utf-8')


# Usage
def basic_encryption():

    message = 'My Hero - Foo Fighters'

    # Setup encryption
    private_key = generate_private_key()
    encryption = create_fernet_model(private_key)

    # Perform encryption and decryption
    encrypted_message = encrypt(message, encryption)
    decrypted_message = decrypt(encrypted_message, encryption)

    # Display output
    print(f'private key: {private_key}')
    print('\n')
    print(f'message: {message}')
    print(f'encrypted message: {encrypted_message}')
    print(f'decrypted message: {decrypted_message}')


basic_encryption()






