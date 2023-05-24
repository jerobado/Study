# Cryptography

List of major cryptography APIs in .NET:
- Windows Data Protection (DPAPI)
- Hashing
- Symmetric encryption
- Public key encryption and signing


## Symmetric encryption

Sample code to encrypt/decrypt string:
```C#
namespace Security;

public class Encryption
{
    public static byte[] Key { get; set; }
    public static byte[] IV { get; set; }

    public static string Encrypt(string plaintext)
    {
        byte[] ciphertext;

        using (Aes model = Aes.Create())
        {
            model.Key = Key;
            model.IV = IV;

            ICryptoTransform encryptor = model.CreateEncryptor(model.Key, model.IV);

            using (MemoryStream memoryStream = new MemoryStream())
            {
                using (CryptoStream cryptoStream = new CryptoStream(memoryStream, encryptor, CryptoStreamMode.Write))
                {
                    using (StreamWriter streamWriter = new StreamWriter(cryptoStream))
                    {
                        streamWriter.Write(plaintext);
                    }
                    ciphertext = memoryStream.ToArray();
                }
            }
        }

        return Convert.ToBase64String(ciphertext);
    }

    public static string Decrypt(string ciphertext) 
    {
        string plaintext;
        byte[] ciphertextBytes = Convert.FromBase64String(ciphertext);

        using (Aes model = Aes.Create())
        {
            model.Key = Key;
            model.IV = IV;

            ICryptoTransform decryptor = model.CreateDecryptor(model.Key, model.IV);

            using (MemoryStream memoryStream = new MemoryStream(ciphertextBytes))
            {
                using (CryptoStream cryptoStream = new CryptoStream(memoryStream, decryptor, CryptoStreamMode.Read))
                {
                    using (StreamReader streamReader = new StreamReader(cryptoStream))
                    {
                        plaintext = streamReader.ReadToEnd();
                    }
                }
            }
        }

        return plaintext;
    }

    public static void GenerateKeys()
    {
        Aes AES = Aes.Create();
        Key = AES.Key;
        IV = AES.IV;
    }
}
```

# References
- [.NET cryptograpy model](https://learn.microsoft.com/en-us/dotnet/standard/security/cryptography-model)
- [Aes Class](https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.aes?view=net-7.0)