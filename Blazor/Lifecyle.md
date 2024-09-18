# Lifecyle
- The Razor component processes Razor component lifecycle events in a set of synchronous and asynchronous lifecycle methods.
- The lifecycle methods can be overridden to perform additional operations in components during component initialization and rendering.

### Events
`SetParametersAsync`
- will be executed if the user entered an argument in the URL route. 

#### Example
```C#
@page "/set-parameters-async/{Param?}"

<PageTitle>Set Parameters Async</PageTitle>

<p>@message</p>


@code {
    [Parameter]
    public string? Param { get; set; }

    private string message = "Not set";

    public override async Task SetParametersAsync(ParameterView parameters)
    {
        if (parameters.TryGetValue<string>(nameof(Param), out var value))
        {
            if (value is null)
                message = "The value of 'Param' is null.";
            else
                message = $"The value of 'Param' is {value}.";
        }

        await base.SetParametersAsync(parameters);
    }

}

// Usage
// /set-parameters-async/hello
// /set-parameters-async/
```

`OnInitialized{Async}`

`OnParametersSet{Async}`

`OnAfterRender{Aync}`

### References
- [ASP.NET Core Razor component lifecycle](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/lifecycle?view=aspnetcore-8.0)