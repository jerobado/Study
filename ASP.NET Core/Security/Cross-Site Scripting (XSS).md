# Cross-Site Scripting (XSS)
- is a security vulnerability which enables an attacker to place client side scripts (usually JavaScript) into web pages
- when other users load affected pages the attacker's scripts will run, enabling the attacker to steal cookies and session tokens, change the contents of the web page through DOM manipulation or redirect the browser to another page
- XSS vulnerabilities generally occur when an application takes user input and outputs it to a page without validating, encoding or escaping it

# Prevention

- Ensure that you only use `@` in an HTML context, not when attempting to insert untrusted input directly into JavaScript
    ```C#
    // .cshtml
    @{
        var untrustedInput = "<\"123\">";
    }

    @untrustedInput

    // when rendered in .html
    &lt;&quot;123&quot;&gt;
    ```

- Don't use untrusted input as part of a URL path. Always pass untrusted input as a query string value

    ```C#
    var example = "\"Quoted Value with spaces and &\"";
    var encodedValue = _urlEncoder.Encode(example);

    // After encoding the encodedValue variable will contain %22Quoted%20Value%20with%20spaces%20and%20%26%22.
    ```

- Always encode untrusted input before output, no matter what validation or sanitization has been performed.

# Resources
- [Prevent Cross-Site Scripting (XSS) in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/cross-site-scripting?view=aspnetcore-6.0)