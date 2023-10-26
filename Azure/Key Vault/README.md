Azure KeyVault API
---
- is a cloud service for securely storing and accessing secrets
- a secret can be your API keys, passwords, certificates, or cryptographic keys

Example
```C#
using Azure.Security.KeyVault.Secrets;

var keyVaultEndpoint = new Uri("<enter URI>");
var client = new SecretClient(keyVaultEndpoint, new DefaultAzureCredential());

builder.Configuration.AddAzureKeyVault(keyVaultEndpoint, new DefaultAzureCredential());

KeyVaultSecret superSecret = client.GetSecret("secretName");
var mySuperSecret = superSecret.Value;
```


# Resources
- [Azure Key Vault basic concepts](https://learn.microsoft.com/en-us/azure/key-vault/general/basic-concepts)
- [Secretless apps with .NET and Azure Key Vault (video)](https://www.youtube.com/watch?v=f8Hf-YUrC10)
- [Azure Identity client library for .NET - version 1.10.1](https://learn.microsoft.com/en-us/dotnet/api/overview/azure/identity-readme?view=azure-dotnet)
- [Grant your app access to Key Vault](https://learn.microsoft.com/en-us/azure/azure-app-configuration/use-key-vault-references-dotnet-core?tabs=core6x#grant-your-app-access-to-key-vault)