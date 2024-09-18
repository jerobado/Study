# Lifecyle
- The Razor component processes Razor component lifecycle events in a set of synchronous and asynchronous lifecycle methods.
- The lifecycle methods can be overridden to perform additional operations in components during component initialization and rendering.

### Events
`SetParametersAsync`
- will be executed if the user entered an argument in the URL route. 

#### Example

_SetParamsAsync.razor_:

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
- will be executed during page initialization

#### Example

_OnInit.razor_:

```c#
@page "/on-initialized"

<PageTitle>On Initialized</PageTitle>

<h3>On Initialized Example</h3>

<p>@message</p>

@code {
    private string? message;

    protected override void OnInitialized()
    {
        message = $"Initialized at {DateTime.Now}.";
    }
}
```


`OnParametersSet{Async}`

`OnAfterRender{Aync}`

### References
- [ASP.NET Core Razor component lifecycle](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/lifecycle?view=aspnetcore-8.0)