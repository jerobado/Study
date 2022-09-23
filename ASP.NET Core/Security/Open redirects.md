# Open Redirects attacks
- a web app that redirects to a URL that's specified via the request such as the querystring or form data can potentially be tampered with to redirect users to an external, malicious URL. This tampering is called an open redirection attack
- whenever your application logic redirects to a specified URL, you must verify that the redirection URL hasn't been tampered with. ASP.NET Core has built-in functionality to help protect apps from open redirect (also known as open redirection) attacks

# Prevention

Use the `LocalRedirect` helper method from the base Controller class:
```C#
public IActionResult SomeAction(string redirectUrl)
{
    return LocalRedirect(redirectUrl);
}
```
`LocalRedirect` will throw an exception if a non-local URL is specified. Otherwise, it behaves just like the Redirect method.

Use the `IsLocalUrl` method to test URLs before redirecting:
```C#
// The following example shows how to check whether a URL is local before redirecting.
private IActionResult RedirectToLocal(string returnUrl)
{
    if (Url.IsLocalUrl(returnUrl))
    {
        return Redirect(returnUrl);
    }
    else
    {
        return RedirectToAction(nameof(HomeController.Index), "Home");
    }
}
```


# Resources
- [Prevent open redirect attacks in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/preventing-open-redirects?view=aspnetcore-6.0)