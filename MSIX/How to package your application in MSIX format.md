# How to package your Qt application in MSIX format

1. Create `appxmanifest.xml` file

2. Run MakeAppx.exe
    ```
    MakeAppx pack /v /h SHA256 /d "eddy-release" /p eddy-package.msix
    ```

3. Create a self-signed certificate 
    ```powershell
    New-SelfSignedCertificate -Type Custom -Subject "CN=Contoso Software, O=Contoso Corporation, C=US" -KeyUsage DigitalSignature -FriendlyName "Your friendly name goes here" -CertStoreLocation "Cert:\CurrentUser\My" -TextExtension @("2.5.29.37={text}1.3.6.1.5.5.7.3.3", "2.5.29.19={text}")
    ```
    ```powershell
    $password = ConvertTo-SecureString -String <Your Password> -Force -AsPlainText 
    Export-PfxCertificate -cert "Cert:\CurrentUser\My\<Certificate Thumbprint>" -FilePath <FilePath>.pfx -Password $password
    ```

4. Sign your package

### Troubleshooting
- https://beebom.com/how-fix-publisher-could-not-be-verified-error-windows-11/