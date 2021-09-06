# ASP.NET Core
_ASP.NET Core_ is an open source, cross-platform web framework for building web applications.

# Definition of terms/concept

**Application logic**
- things that implement your business logic in your application

**Application model**
- it's a typically a whole group of different services and classes and is more of a concept -- anything needed to perform some sort of business action in your application.

**Ambient values**
- are the route values for the current request. They include controller and action when called from an MVC controller but can also include additional route values that were set when the action or Razor Page was initially located using routing.

**Binding model**
- extract values from a request and uses them to create .NET object.
- is one or more objects that act as a "container" for the data provided in a request -- data that's required by a page handler
- input to a Razor page
- is all the information that's provided by the user when making a request, as well as additional contextual data.
- model binding is great for reducing repetitive code
- there a two (2) different ways to use model binding in Razor Pages:
    1. Decorate properties on your PageModel witht the `[BindProperty]` attribute
    2. Add parameters to your page handler method.

**Blazor**
- is a framework that allows you to build interactive client-side web applications by either leveraging the WebAssembly standard to run .NET code directly in your browser, or by using a stateful model with SignalR

**Business logic**
- business rule or requirements that needs to be implemented in your application

**Cache-busting query string**
- adds a query parameter to a URL, such as `?v=1`
- browser will cache the response and use it for subsequent requests to the URL
- when resource changes, the query string is also changed, for example to `?v=2`
- browser will see this as a request for a new resource and will make a fresh request
- `asp-append-version="true"`:
    - this attribute will load the file being referenced and generate a unique hash based on its contents
    - i.e. `<script src="/js/site.js?v=EWaMeWsJBYWmL2g_KkgXZQ5nPe"></script>`

**Cross-site request forgery (CSRF)**
- are attack exploits on a website that can allow actions to be executed on your website by an unrelated malicious website.

**DataAnnotations**
- handy attributes that creates validation for your fields
- System.Components.DataAnnotations
- i.e. `[Required]`, `[EmailAddress]`, `[Phone]`, etc.
- are good for input validation of properties in isolation, but not so good for validating business roles

**Dependency Injection or the Inversion of Control (IoC)**
- is a software engineering technique in which an object (client) uses another object's method (services)

**Directive**
- is a statement in a Razor file that changes the way the template is parsed or compiled.
- i.e. `@using <namespace>` directive, which makes objects in the `<namespace>` avaialable.

**Endpoint**
- is some handler that returns a reponse
- each endpoint is associated with a URL pattern
- its your application's units of executable request-handling code

**Implicit Page Handler**
- a page handler that gets executed by the EndpointMiddleware when no request has been matched.
- it takes part in model binding and use page filter but execute no logic.

**Internet Information Services (IIS)**
- extensible web server for the Windows NT family.

**Kestrel**
- a cross-platform HTTP server where ASP.NET Core can run

**Layout**
- is a template that includes common code
- it can't be rendered directly, but it can be rendered in conjuction with a normal Razor views.

**Metadata**
- describes other data, specifying the rules and characteristics the data should adhere to

**Middleware**
- consists of small components that execute in sequence when the application receives an HTTP request. They can perform a whole host of functions, such as logging, identifying the current user for a request, serving static files, and handling errors.
- are C# classes or functions that handle an HTTP request or response. They are chained together, with the output of one middleware acting as the input to the next middleware, to form a pipeline.

**Model binding**
- the process of extracting values from a request and converting them to .NET types

**MVC (Model-View-Controller)**
- for building Web APIs
- a common pattern for designing apps that have User Interfaces (UI)
- it aims to separate the management and manipulation of data from its visual representation
- it's all about separation of concern
- `MODEL`:
    - the data that needs to be displayed
    - responsible to represent the state of the application and any business logic or operations that should be performed
    - business logic should be encapsulated in the model along with any implementation logic persisting the state of application
- `VIEW`:
    - is reponsible for generating the final representation of the data
    - responsible for **<ins>presenting content</ins>** through the user interface
    - it uses Razor view engine to embed .NET code in HTML markup
    - there should be minimal logic within views, and any logic in them should relate to presenting content
    - use View Component, ViewModel, or view template to simply complex views
    - it shouldn't call methods in the `PageModel` -- the view should generally only be accessing data that has already been collected and exposed as properties
- `CONTROLLER`:
    - orchestrate what MODEL to use and which VIEW to represent
    - handles and responds to user input and interaction
    - controllers shouldn't be overly complicated by too many responsibilities
    - push business logic out of the controller if its becoming overly complex into the domain model

**MVC controller**
- is a class that contains a number of logically grouped action methods
- action or action methods is a method that runs in response to a request
- action method on an MVC controller

**Page handler**
- is a method that runs in response to a request. Razor Page models must be derived from the PageModel class. They can contain multiple page handlers, though typically they only contain one or two.
- page handler on a Razor page
- each Razor Page typically handles a single _route_, but it can handle multiple HTTP verbs like `GET` and `POST`.
- each page handler typically handles a single HTTP verb.

**Page-based websites**
- websites that user can browse multiple pages, enters data into forms, and generally consumes content

**PageModel**
- this is where you define the binding models for a page, which extracts data from the incoming request.
- it's also where you defing the page's page handlers

**Partial views**
- are a bit like Razor Pages without the `PageModel` and handlers
- they are purely about rendering small sections of HTML, rather than handling requests, model binding, and validation, cand calling the application model
- they are great for encapsulating small usable bits of HTML that you need to generate on multiple Razor Pages

**Pipeline**
- the process wherein a piece of middleware can call another piece of middleware, which in turn can call another, and so on.

**Project**
- is a unit of deployment, which will be compiled into a .dll file or an executable. Each separate app is a separate project. Multiple projects can be built and developed at once ina solution

**Query string**
- is a part of a URL that contains additional data that doesn't fit in the path, i.e. `/product?name=big-widget`, or `/product?id=12`

**Razor Pages**
- server-side rendered "page-based" websites
- contain business logic, load data from a database, or use forms to allow user to submit information
- generally refers to the page-based paradigm that combines routing, model binding and HTML generation using Razor views
- a **<ins>Razor Page</ins>** represents a single "endpoint". It typically consists of two files: a `.cshtml` file containing the Razor view, and a `.cshtml.cs` file containing the page's `PageModel`.

**Razor view**
- also called Razor templates are used to generate HTML
- they are typically used in the final stage of a Razor Page to generate the HTML response to send back to the user.
- use `@model <modelname>` to access the model and render it to the user

**Reflection**
- in .NET allows you to obtain information about types in your application at runtime. You can use reflection to create instance of classes at runtime and to invoke and access them.

**Reverse proxy**
- external HTTP server outside your ASP.NET Core application (i.e. IIS, Apache HTTP, NGINX, etc.)

**Route template**
- is a URL pattern that is used to match against request URLs. They're strings of fixed values, like `/test`.
- they can have placeholders for variables that can contain optional values

**Route values**
- are the values extracted from a URL based on a given route template

**Routing**
- is the process of mapping an incoming request to a method that will handle it
- is the selection of Razor page to invoke in response to a given request
- is the process of mapping an income HTTP request to a specific handler

**Segment**
- is a small contiguous section of a URL. It's separated from other URL segment by at least one character, often by the "/" character.

**Services**
- within the context of ASP.NET Core, it refers to any class that provides functionality to an application. These could be classes exposed by a library or code you've written for your application.

**Single-page Applications (SPA)**
- websites with heavily interactive on the client side like games

**Single Responsiblity Principle (SRP)**
- states that every class should be responsible for only a single piece of functionality -- it should only need to change if that required functionality changes.

**Tag Helpers**
- are extra attributes on standard HTML elements (or new elements entirely) that work by modifying the HTML elements they're attached to.
- they can modify the HTML element they're attached to, but they can't modify anything else on your page.
- simplify the fiddly mechanics of building forms

**Template**
- basic code required to build an application

**ViewImports**
- `_ViewImports.cshtml` file contains directive that will be inserted at the top of every view.
- to avoid adding `@using` statements to every view
- should be located in the root of Pages folder

**ViewStart**
- `_ViewStart.cshtml` file contains C# arbitrary code at the start of every view in your application.
- should be located in the root of Pages folder

**wwwroot**
- is a special folder wherein the browser is only allowed to access. This file include static files like CSS, JavaScript, images or static HTML file

# References
All of the contents herein are based on the following:
- [ASP.NET Core in Action, 2nd Edition](https://www.manning.com/books/asp-net-core-in-action-second-edition) by Andrew Lock
- [ASP.NET Documentation](https://docs.microsoft.com/en-us/aspnet/core/?view=aspnetcore-5.0) by Microsoft