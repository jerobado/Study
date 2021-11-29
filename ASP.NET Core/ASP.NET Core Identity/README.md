# ASP.NET Core Identity
- is an API that supports user interface (UI) login functionality
- manages uers, passwords, profile data, roles, claims, token, email confirmation, and more

### Benefits
- users can create an account with the login information stored in Identiy or they can use an external login provide like _Facebook_, _Google_, _Microsoft Account_ and _Twitter_.

# Tutorials

## How to add ASP.NET Core Identity to an existing project?

1. Add the following NuGet packages to your project:
    * `Microsoft.AspNetCore.Identity.EntityFrameworkCore` - core Identity services and integration with EF Core
    * `Microsoft.AspNetCore.Identity.UI` - UI Razor Pages
2. Update your `Startup.cs` file by adding the following code:
    ```C#
    // ApplicationUser is your custom IdentityUser
    services.AddDefaultIdentity<ApplicationUser>(options => options.SignIn.RequireConfirmedAccount = true)
            .AddEntityFrameworkStores<AppDbContext>();
    ```
3. Add the `AuthenticationMiddleware` in your `Configure` method:
    ```C#
    app.UserRouting();
    
    // Order is important here
    app.UseAuthentication();
    app.UseAuthorization();

    app.UseEndpoints();
    ```
4. Create the `Applicationuser` in the Data folder:
    ```C#
    public class ApplicationUser : IdentityUser { }
    ```
5. Update your `DBContext`
    ```C#
    public class AppDbContext : IdentityDbContext<ApplicationUser> { }
    ```
6. Add a new migration to reflect your changes to the database:
    ```
    // dotnet CLI
    dotnet ef migrations add AddIdentitySchema

    // Visual Studio
    Add-Migration AddIdentitySchema
    ```
7. Update the Razorz views to link to the Identity UI

# Glossary

**Authentication**
- the process of creating users and letting them log in to your app
- the process of determining _who you are_

**Authorization**
- customizing the experience and controlloing what user's can do, based on the current logged-in user
- the process of determining _what you're allowed to do_

**claim**
- is a single piece of information about a principal
- it consists of a _claim type_ and a an optional _value_

**cookie**
- is a small piece of text that's sent back and fort between the browser and your app along with each request, consisting of a name and a value

**principal**
- every request is associated with a user called _principal_
- is the current user, implemented as `ClaimsPrincipal` class
- it contains a collection of `Claims` that describe the user

**scaffolding**
- is the process of generating files in your project that serve as the basis for customization

**Two-factor authentication (2FA)**
- is where you require an extra piece of information to sign in, in addition to a password
- e.g., sending a code to a user's phone by SMS, or using a mobile app to generate a code
