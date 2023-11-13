# How to implement DocuSign Embedded Signing through your app

### Pre-requisite
- DocuSign developer account
- App and Integration Keys in DocuSign account

#### 1. Install DocuSign.eSign.dll package via Nuget

#### 2. Authenticate via JWT Grant

#### 3. Make Envelope

#### 4. Create the recipient view and initiate embedded signing

#### 5. Redirect within your app


### DocuSign Developer Account

1. Navigate to Integration > Apps and Keys > Actions > Edit of your selected app
2. Take note of the newly created Integration Keys
3. In Service Integration, click the Generate RSA button
4. Copy the Private Key and securely save it in a file 
4. Add Redirect URIs
3. Click the Save button

### Visual Studio

1. Install DocuSign via Nuget

    ```
    Install-Package DocuSign.eSign.dll -Version 6.8.0
    ```

2. Add **DocuSignJWT** option in `appsettings.json` file:

    ```json
      "DocuSignJWT": {
        "ClientId": "Integration Key",
        "ImpersonatedUserId": "User ID",
        "AuthServer": "account-d.docusign.com",
        "PrivateKeyFile": "/path/to/your/private.key",
        "SignerEmail": "email address",
        "SignerName": "full name"
    }
    ```

    You can get the details in your DocuSign Developer account.

# Resources
- [How to request a signature through your app](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-in-app-embedded/)