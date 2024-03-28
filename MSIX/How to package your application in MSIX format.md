# How to package your Qt application in MSIX format

1. Create `appxmanifest.xml` file inside your package

2. Generate a Package Resource Index (PRI) file using MakePri
    ```powershell
    makepri createconfig /cf priconfig.xml /dq en-US

    makepri new /pr path/to/your/package /cf priconfig.xml
    ```

2. Test your application before packaging
    ```powershell
    Add-AppxPackage –Register AppxManifest.xml
    ```

3. Run `MakeAppx.exe` tool to create an MSIX package
    ```powershell
    MakeAppx pack /v /h SHA256 /d path/to/your/package /p installer.msix
    ```

**Optional**: you may proceed to the next steps below if you wish to self-sign your `.msix` package. You can already submit your `.msix` package in the Microsoft Store without self-signing.

5. Create a self-signed certificate 
    ```powershell
    New-SelfSignedCertificate -Type Custom -Subject "CN=Contoso Software, O=Contoso Corporation, C=US" -KeyUsage DigitalSignature -FriendlyName "Your friendly name goes here" -CertStoreLocation "Cert:\CurrentUser\My" -TextExtension @("2.5.29.37={text}1.3.6.1.5.5.7.3.3", "2.5.29.19={text}")
    ```
    ```powershell
    $password = ConvertTo-SecureString -String <Your Password> -Force -AsPlainText 
    
    Export-PfxCertificate -cert "Cert:\CurrentUser\My\<Certificate Thumbprint>" -FilePath <FilePath>.pfx -Password $password
    ```

6. Sign your package
    ```powershell
    SignTool sign /fd SHA256 /a /f path/to/certificate.pfx /p mypassword path/to/package.msix
    ```

### Reminders
- your package identity, family and publisher name must match the Package Identity in Microsoft Store
- `<DisplayName>` should match the name of the application that you reserved in Microsoft Store

### Troubleshooting
- https://beebom.com/how-fix-publisher-could-not-be-verified-error-windows-11/
- https://stackoverflow.com/questions/23812471/installing-appx-without-trusted-certificate
- https://juniperphoton.dev/how-to-set-unplated-icon-for-uwp-apps/

### References
- [Package from the command line](https://learn.microsoft.com/en-us/windows/msix/package/manual-packaging-root)