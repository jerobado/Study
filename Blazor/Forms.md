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

## Handle Form Submission
The `EditForm` provides the following callbacks for handling form submission:

- Use `OnValidSubmit` to assign an event handler to run when a form with valid fields is submitted.
- Use `OnInvalidSubmit` to assign an event handler to run when a form with invalid fields is submitted.
- Use `OnSubmit` to assign an event handler to run regardless of the form fields' validation status. The form is validated by calling `EditContext.Validate` in the event handler method. If Validate returns `true`, the form is valid.

## Antiforgery support
- Antiforgery services are automatically added to Blazor apps when `AddRazorComponents` is called in the Program file.
- For forms based on `EditForm`, the **AntiforgeryToken** component and `[RequireAntiforgeryToken]` attribute are automatically added to provide antiforgery protection.

### References
- [ASP.NET Core Blazor forms overview](https://learn.microsoft.com/en-us/aspnet/core/blazor/forms/?view=aspnetcore-8.0)