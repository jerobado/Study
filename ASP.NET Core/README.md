ASP.NET Core
---
_ASP.NET Core_ is an open source, cross-platform web framework for building web applications.

Definition of terms/concept
---

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

**DataAnnotations**
- handy attributes that creates validation for your fields
- System.Components.DataAnnotations
- i.e. `[Required]`, `[EmailAddress]`, `[Phone]`, etc.
- are good for input validation of properties in isolation, but not so good for validating business roles

**Dependency Injection or the Inversion of Control (IoC)**
- is a software engineering technique in which an object (client) uses another object's method (services)

**Endpoint**
- is some handler that returns a reponse. Each endpoint is associated with a URL pattern.

**Implicit Page Handler**
- a page handler that gets executed by the EndpointMiddleware when no request has been matched.
- it takes part in model binding and use page filter but execute no logic.

**Internet Information Services (IIS)**
- extensible web server for the Windows NT family.

**Kestrel**
- a cross-platform HTTP server where ASP.NET Core can run

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
- MODEL: the data that needs to be displayed
- VIEW: is reponsible for generating the final representation of the data
- CONTROLLER: orchestrate the MODEL and VIEW

**MVC controller**
- is a class that contains a number of logically grouped action methods
- action or action methods is a method that runs in response to a request
- action method on an MVC controller

**Reflection**
- in .NET allows you to obtain information about types in your application at runtime. You can use reflection to create instance of classes at runtime and to invoke and access them.

**Reverse proxy**
- external HTTP server outside your ASP.NET Core application (i.e. IIS, Apache HTTP, NGINX, etc.)

**Page-based websites**
- websites that user can browse multiple pages, enters data into forms, and generally consumes content

**Page handler**
- is a method that runs in response to a request. Razor Page models must be derived from the PageModel class. They can contain multiple page handlers, though typically they only contain one or two.
- page handler on a Razor page

**Pipeline**
- the process wherein a piece of middleware can call another piece of middleware, which in turn can call another, and so on.

**Project**
- is a unit of deployment, which will be compiled into a .dll file or an executable. Each separate app is a separate project. Multiple projects can be built and developed at once ina solution

**Query string**
- is a part of a URL that contains additional data that doesn't fit in the path, i.e. `/product?name=big-widget`, or `/product?id=12`

**Razor Pages**
- server-side rendered "page-based" websites
- contain business logic, load data from a database, or use forms to allow user to submit information

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

**Template**
- basic code required to build an application

**wwwroot**
- is a special folder wherein the browser is only allowed to access. This file include static files like CSS, JavaScript, images or static HTML file
