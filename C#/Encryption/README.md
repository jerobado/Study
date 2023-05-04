# Encryption

Sample code to encrypt/decrypt string:
```C#
public class Security
    {
        public static byte[] Key { get; set; }
        public static byte[] IV { get; set; }

        public static string Encrypt(string plaintext)
        {
            // TODO: create an encryption model
            Aes model = Aes.Create();
            model.Key = Key;
            model.IV = IV;

            return plaintext;
        }

        public static string Decrypt(string ciphertext) 
        {
            return ciphertext;
        }

        public static Aes CreateAES()
        {
            Aes AES = Aes.Create();
            Key = AES.Key;
            IV = AES.IV;

            return AES;
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