# Fluent UI Blazor

Getting Started

1. Install package via Nuget

    ```
    dotnet add package Microsoft.FluentUI.AspNetCore.Components
    ```

2. Add `Microsoft.FluentUI.AspNetCore.Components` in `_Imports.razor`:

    ```c#
    @using Microsoft.FluentUI.AspNetCore.Components
    ```

3. Register the service in `Program.cs`

    ```c#
    builder.Services.AddFluentUIComponents();
    ```

4. Add component providers in `MainLayout.razor`

    ```c#
    <FluentToastProvider />
    <FluentDialogProvider />
    <FluentTooltipProvider />
    <FluentMessageBarProvider />
    <FluentMenuProvider />
    ```

5. Test Fluent UI Blazor components in `Home.razor`

    ```html
    <FluentCard Width="350px" Height="250px">
        <h2>Hello World!</h2>
        <FluentButton Appearance="@Appearance.Accent">Click Me</FluentButton>
    </FluentCard>
    ```


### References
- [Code Setup - FluentUI Blazor Components](https://www.fluentui-blazor.net/CodeSetup)