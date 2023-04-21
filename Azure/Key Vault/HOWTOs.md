# How Tos


## How to create and configure Azure Key Vault using PowerShell and Azure CLI?
1. Create the Key Vault:

    ```powershell
    > New-AzKeyVault -VaultName 'unique-keyvault-name' -ResourceGroupName 'resource-name' -Location 'location'
    ```

2. Give yourself permissino to access the serets with your email:

    ```powershell
    > Set-AzKeyVaultAccessPolicy -VaultName 'unique-keyvault-name' -UserPrincipalName '<Email>' -PermissionsToSecrets Set,Get,List
    ```

3. Add a secret message to your vault:

    ```powershell
    > $SecretMessage = ConvertTo-SecureString -String 'Your secret code is XYZ123!' -AsPlainText -Force
    > $KVSecret = Set-AzKeyVaultSecret -VaultName $KVName -Name 'SecretMessage' -SecretValue $SecretMessage
    ```

4. Create an App Configuration reference to your new secret:

    ```powershell
    > az appconfig kv set-keyvault --name $ACSName --key SecretMessage --secret-identifier $KVSecret.Id --yes
    ```

5. Display you key vault details:

    ```powershell
    > Get-AZKeyVault -VaultName 'unique-keyvault-name'
    ```