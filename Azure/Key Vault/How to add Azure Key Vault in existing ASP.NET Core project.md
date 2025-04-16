# How to add Azure Key Vault in existing ASP.NET Core project

In Azure Portal
1. Create Azure Key Vault resource
2. Create secrets in _**key-vault-name**_ > **Objects** > **Secrets**


In your ASP.NET Core project

1. Install packages

    ```
    Azure.Security.KeyVault.Secrets
    Azure.Identity
    ```

2. In `Program.cs`
    ```c#
    using Azure.Identity;
    using Azure.Security.KeyVault.Secrets;

    var keyVaultUri = new Uri("https://<keyvault-name>.vault.azure.net/");
    var client = new SecretClient(keyVaultUri, new DefaultAzureCredential());

    builder.Configuration.AddAzureKeyVault(keyVaultUri, new DefaultAzureCredential());

    KeyVaultSecret superSecret = client.GetSecret("<secret-name>");
    var mySuperSecret = superSecret.Value;

    ```