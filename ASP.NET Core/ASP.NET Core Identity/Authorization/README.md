# Authorization

The `AuthorizationMiddleware` is reponsible for applying authorization requirements and ensuring that only authorized user can execute protected endpoints.

# How to use simple Authorization in ASP.NET Core?

You can achieve a basic level of authorization by using the `[Authorize]` attribute. You can apply this as follows:

1. Action-based authorization

    ```C#
    public class RecipeApiController: ControllerBase
    {
        // This action can be executed by anyone, even when not logged in.
        public IActionResult List()
        {
            return Ok();
        }

        // This action can only be executed by authenticated users.
        [Authorize]
        public IActionResult View()
        {
            return Ok();
        }
    }
    ```

2. Controller-based authorization

    ```C#
    [Authorize]
    public class AccountController : Controller
    {
        public ActionResult Login()
        {
        }

        public ActionResult Logout()
        {
        }
    }
    ```

3. Using `[AllowAnonymous]` attribute

    ```C#
    [Authorize]
    public class AccountController : Controller
    {
        [AllowAnonymous]
        public ActionResult Login()
        {
        }

        public ActionResult Logout()
        {
        }
    }
    ```

    **Warning**:

    `[AllowAnonymous]` bypasses all authorization statements. If you combine `[AllowAnonymous]` and any `[Authorize]` attribute, the `[Authorize]` attributes are ignored. For example if you apply `[AllowAnonymous]` at the controller level, any `[Authorize]` attributes on the same controller (or on any action within it) is ignored.

# Handling unauthorized requests

The `AuthorizationMiddleware` generates the following response depending on type of requests:

1. **Authorized**
    - If authorization is successful, the endpoint executes and generates a response as normal.

2. **Challenge**
    - this response indicates the user was not authorized to execute the
action because they weren’t yet logged in.

3. **Forbid**
    - this response indicates that the user was logged in but didn’t meet the
requirements to execute the action. They didn’t have a required claim, for
example.

# Glossary

**endpoint**
- refers to the handler selected by the routing middleware, which will generate a response when executed
- typically a Razor Page or a Web API action method


# References
- [Simple authorization in ASP.NET Core](https://docs.microsoft.com/en-us/aspnet/core/security/authorization/simple?view=aspnetcore-6.0)