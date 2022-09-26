# Cross-Site Request Forgery (XSRF-CSRF)
- Cross-site request forgery (also known as XSRF or CSRF) is an attack against web-hosted apps whereby a malicious web app can influence the interaction between a client browser and a web app that trusts that browser.
- These attacks are possible because web browsers send some types of authentication tokens automatically with every request to a website.
- This form of exploit is also known as a one-click attack or session riding because the attack takes advantage of the user's previously authenticated session.

# Prevention

Implement Antiforgery in ASP.NET Core forms especially on **POST** requests
```C#
[HttpPost]
[ValidateAntiForgeryToken]
public IActionResult Index()
{
    // ...

    return RedirectToAction();
}
```

# Resource
- [Prevent Cross-Site Request Forgery (XSRF/CSRF) attacks in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/anti-request-forgery?view=aspnetcore-6.0)