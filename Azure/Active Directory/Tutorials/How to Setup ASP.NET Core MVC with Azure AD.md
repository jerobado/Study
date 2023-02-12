# How to Setup ASP.NET Core MVC with Azure AD

### Requirements
- Microsoft Azure account
- Working ASP.NET Core MVC application

**In Azure Portal**

1. Create a new tenant for your application in Azure AD. Go to **Active Azure Directory** > **Manage tenants** > **Create a tenant** and fill in the details

2. In your current Active Directory,
    - go to Enterprise applications > New application > Create your own application
    - enter the app name
    - select **Register an application to integrate with Azure AD (App you're developing)**
    
    Register an application
    - select **Accounts in this organizational directory only (Study Azure AD only - Single tenant)**
    - Select a platform: Web
    - URL: https://localhost:&lt;port number&gt;/signin-oidc

3. Set ID tokens
    - App registration > select your application
    - Authentication > Implicit grant and hybrid flows section
    - Check **ID tokens (used for implicit and hybrid flows)**

**In Visual Studio**

1. Install dependencies via nuget package manager
    ```
    Microsoft.AspNetCore.Authentication.JwtBearer
    Microsoft.AspNetCore.Authentication.OpenIdConnect
    Microsoft.Identity.Web
    Microsoft.Identity.Web.UI
    ```

2. Configure **AzureAd** settings in your `appsettings.json` file
    ```json
    {
        "AzureAd": {
            "Instance": "https://login.microsoftonline.com/",
            "Domain": "your.awesome.domain",
            "TenantId": "",
            "ClientId": "",
            "CallbackPath": "/signin-oidc"
        }
    }
    ```

3. Update your `Program.cs` file
    ```C#
    // Use Azure AD
    builder.Services.AddAuthentication(OpenIdConnectDefaults.AuthenticationScheme)
        .AddMicrosoftIdentityWebApp(builder.Configuration.GetSection("AzureAd"));

    // Add services to the container.
    builder.Services.AddControllersWithViews(options =>
    {
        var policy = new AuthorizationPolicyBuilder()
            .RequireAuthenticatedUser()
            .Build();
        options.Filters.Add(new AuthorizeFilter(policy));
    });
    builder.Services.AddRazorPages().AddMicrosoftIdentityUI();
    
    ...
    
    app.UseAuthentication();    // add in this order
    app.UseAuthorization();
    ```

# Resources
- [Create an ASP.NET Core Web App using Azure AD Authentication](https://blog.matrixpost.net/create-an-asp-net-core-web-app-model-view-controller-using-azure-ad-authentication/)
- [Quickstart: Create a new tenant in Azure Active Directory](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-access-create-new-tenant)