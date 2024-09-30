# Blazor Forms

### Example

_StarshipPlainForm.razor_
```c#
@page "/starship-plain-form"
@inject ILogger<StarshipPlainForm> Logger

<form method="post" @onsubmit="Submit" @formname="starship-plain-form">
    <AntiforgeryToken />
    <div>
        <label>
            Identifier: 
            <InputText @bind-Value="Model!.Id" />
        </label>
    </div>
    <div>
        <button type="submit">Submit</button>
    </div>
</form>

@code {
    [SupplyParameterFromForm]
    private Starship? Model { get; set; }

    protected override void OnInitialized() => Model ??= new();

    private void Submit()
    {
        Logger.LogInformation("Id = {Id}", Model?.Id);
    }

    public class Starship
    {
        public string? Id { get; set; }
    }
}
```

In the preceding StarshipPlainForm component:

- The form is rendered where the <form> element appears. The form is named with the @formname directive attribute, which uniquely identifies the form to the Blazor framework.
- The model is created in the component's @code block and held in a public property (Model). The [SupplyParameterFromForm] attribute indicates that the value of the associated property should be supplied from the form data. Data in the request that matches the property's name is bound to the property.
- The InputText component is an input component for editing string values. The @bind-Value directive attribute binds the Model.Id model property to the InputText component's Value property.
- The Submit method is registered as a handler for the @onsubmit callback. The handler is called when the form is submitted by the user.

Instead of using plain forms in Blazor apps, use Blazor's built-in component `EditForm` instead:

```c#
@page "/starship-1"
@inject ILogger<Starship1> Logger

<EditForm Model="Model" OnSubmit="Submit" FormName="Starship1">
    <div>
        <label>
            Identifier:
            <InputText @bind-Value="Model!.Id" />
        </label>
    </div>
    <div>
        <button type="submit">Submit</button>
    </div>
</EditForm>

@code {
    [SupplyParameterFromForm]
    private Starship? Model { get; set; }

    protected override void OnInitialized() => Model ??= new();

    private void Submit()
    {
        Logger.LogInformation("Id = {Id}", Model?.Id);
    }

    public class Starship
    {
        public string? Id { get; set; }
    }
}
```


### References
- [ASP.NET Core Blazor forms overview](https://learn.microsoft.com/en-us/aspnet/core/blazor/forms/?view=aspnetcore-8.0)