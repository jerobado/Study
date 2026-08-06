# How to add ASP.NET Core Identity to an existing project?

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