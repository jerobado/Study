# Remote Signing

1. Authenticate via JWT Token
    ```C#
    public OAuthToken Authenticate(string clientId, string userId, string authServer, string privateKeyFile)
    {
        byte[] privateKeyBytes = System.IO.File.ReadAllBytes(privateKeyFile);
        var scopes = new List<string> { "impersonation", "signature" };

        var dsClient = new DocuSignClient();
        var accessToken = dsClient.RequestJWTUserToken(clientId, userId, authServer, privateKeyBytes, 1, scopes);

        return accessToken;
    }
    ```


# Resources
- [How to request a signature by email](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-email-remote/)
- [launcher-csharp/eSignature/Examples/SigningViaEmail.cs](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/eSignature/Examples/SigningViaEmail.cs)