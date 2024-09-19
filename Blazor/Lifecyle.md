# Lifecyle
- The Razor component processes Razor component lifecycle events in a set of synchronous and asynchronous lifecycle methods.
- The lifecycle methods can be overridden to perform additional operations in components during component initialization and rendering.

### Events
`SetParametersAsync`
- Executed if the user entered an argument in the URL route. 

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
- Executed during page initialization

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
- Excecuted after the component is initialized in `OnInitialized` or `OnInitializedAsync`
- When the parent component rerenders and supplies: known or primitive immutable types when at least one parameter has changed; Complex-typed parameters.

#### Example

_OnParamsSet.razor_
```c#
@page "/on-params-set"
@page "/on-params-set/{StartDate:datetime}"

<PageTitle>On Parameters Set</PageTitle>

<h1>On Parameters Set Example</h1>

<p>
    Pass a datetime in the URI of the browser's address bar. 
    For example, add <code>/1-1-2024</code> to the address.
</p>

<p>@message</p>

@code {
    private string? message;

    [Parameter]
    public DateTime StartDate { get; set; }

    protected override void OnParametersSet()
    {
        if (StartDate == default)
        {
            StartDate = DateTime.Now;

            message = $"No start date in URL. Default value applied " +
                $"(StartDate: {StartDate}).";
        }
        else
        {
            message = $"The start date in the URL was used " +
                $"(StartDate: {StartDate}).";
        }
    }
}
```

`OnAfterRender{Aync}`

### References
- [ASP.NET Core Razor component lifecycle](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/lifecycle?view=aspnetcore-8.0)