ASP.NET Core
---
_ASP.NET Core_ is an open source, cross-platform web framework for building web applications.

Definition of terms/concept
---

**Binding model**
- is one or more objects that act as a "container" for the data provided in a request -- data that's required by a page handler

**Dependency Injection or the Inversion of Control (IoC)**
- is a software engineering technique in which an object (client) uses another object's method (services)

**Endpoint**
- is some handler that returns a reponse. Each endpoint is associated with a URL pattern.

**Internet Information Services (IIS)**
- extensible web server for the Windows NT family.

**Kestrel**
- a cross-platform HTTP server where ASP.NET Core can run

**Middleware**
- consists of small components that execute in sequence when the application receives an HTTP request. They can perform a whole host of functions, such as logging, identifying the current user for a request, serving static files, and handling errors.
- are C# classes or functions that handle an HTTP request or response. They are chained together, with the output of one middleware acting as the input to the next middleware, to form a pipeline.

**Model binding**
- the process of extracting values from a request and converting them to .NET types

**MVC (Model-View-Controller)**
- for building Web APIs
- a common pattern for designing apps that have User Interfaces (UI)
- it aims to separate the management and manipulation of data from its visual representation
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
- is a part of a URL that contains additional data that doesn't fit in the path, i.e. "/product?name=big-widget", or "/product?id=12"

**Razor Pages**
- server-side rendered "page-based" websites
- contain business logic, load data from a database, or use forms to allow user to submit information

**Route template**
- is a URL pattern that is used to match against request URLs. They're strings of fixed values, like "/test".
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
