# raw record > encrypt > write to file


from cryptography.fernet import Fernet


key = Fernet.generate_key()
print('key:', key)

model = Fernet(key)

record = b'1'
encrypted_record = model.encrypt(record)


with open('record.txt', 'a') as file:
    file.write(f'{str(encrypted_record)}\n')
