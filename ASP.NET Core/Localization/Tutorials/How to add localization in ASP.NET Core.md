# How to add localization in ASP.NET Core

### Steps

1. Configure Localization service and middleware in `Program.cs`

    ```c#
    builder.Services.AddLocalization(options => options.ResourcesPath = "Resources");

    builder.Services.AddMvc()
        .AddViewLocalization(LanguageViewLocationExpanderFormat.Suffix)
        .AddDataAnnotationsLocalization();
    
    builder.Services.Configure<RequestLocalizationOptions>(options =>
    {
        var supportedCultures = new[] { "en", "ja" };
        options.SetDefaultCulture(supportedCultures[0])
            .AddSupportedCultures(supportedCultures)
            .AddSupportedUICultures(supportedCultures);
    });

    app.UseRequestLocalization();
    ```

2. Create a `Resources` folder in your project

3. In your `Resources` folder, create an `.resx` file for your target language

    For example, if you want to localize your razor pages in English and Japanese, you will create the resource files as follows:

    | Razor page           | Resource file                                                        |
    | -------------------- | -------------------------------------------------------------------- |
    | `Pages/Index.cshtml` | `Resources/Pages.Index.en.resx` <br> `Resources/Pages.Index.jp.resx` |
    | `Pages/About.cshtml` | `Resources/Pages.About.en.resx` <br> `Resources/Pages.Index.jp.resx` |

4. On each `.resx` file, enter your translations

    ![.resx window](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/localization/_static/hola.png?view=aspnetcore-10.0)

5. Use in Razor pages

    In `Pages/Index.cshtml`:

    ```c#
    @inject Microsoft.AspNetCore.Mvc.Localization.IViewLocalizer Localizer

    <h1>@Localizer["Hello"]</h1>
    ```

6. Switch language by passing a query string

    ```
    https://localhost:5001/?culture=en
    https://localhost:5001/?culture=ja
    ```

## References
- [Globalization and localization in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/localization?view=aspnetcore-10.0)