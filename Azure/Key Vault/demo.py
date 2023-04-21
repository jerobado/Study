# Azure Key Vault Demo


from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

vault_url = 'https://geronacapital-keyvault.vault.azure.net/'

# Authenticate via Service Principal with Secret
# - AZURE_TENANT_ID
# - AZURE_CLIENT_ID
# - AZURE_CLIENT_SECRET
credential = DefaultAzureCredential()


secret_client = SecretClient(vault_url=vault_url, credential=credential)
secret = secret_client.get_secret('GERONACAPITAL-DB-HOST')

print(secret.name)
print(secret.value)

