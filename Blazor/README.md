# Blazor
- Blazor is a framework for building interactive client-side web UI with .NET
- Create rich interactive UIs using C# instead of JavaScript.
- Share server-side and client-side app logic written in .NET.
- Render the UI as HTML and CSS for wide browser support, including mobile browsers.
- Integrate with modern hosting platforms, such as Docker.
- Build hybrid desktop and mobile apps with .NET and Blazor.

## Components
- Blazor apps are based on _components_
- A component is an element of UI, such as a page, dialog, or data entry form
- The component class is usually written in the form of a Razor markup page with a `.razor` file extension. 

Example
```HTML
<div class="card" style="width:22rem">
    <div class="card-body">
        <h3 class="card-title">@Title</h3>
        <p class="card-text">@ChildContent</p>
        <button @onclick="OnYes">Yes!</button>
    </div>
</div>

@code {
    [Parameter]
    public RenderFragment? ChildContent { get; set; }

    [Parameter]
    public string? Title { get; set; }

    private void OnYes()
    {
        Console.WriteLine("Write to the console in C#! 'Yes' button selected.");
    }
}
```

# References
- [ASP.NET Core Blazor](https://learn.microsoft.com/en-us/aspnet/core/blazor/?view=aspnetcore-7.0)