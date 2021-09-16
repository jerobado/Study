# Deploying ASP.NET Core

### Objective
- learn how deployment works in ASP.NET Core
- deploy your own application to the Internet


## Hosting Model for ASP.NET Core
- an ASP.NET core applications by the end of the day are basically just console applications
- they have a `static void Main` function that serves as an entry for the application
- what makes an ASP.NET Core app is that it <ins>**runs a web server**</ins>, called _Kestrel_, inside the console app process.
- Kestrel provides the HTTP functionality to receive requests and return responses to clients.



## Definition of Terms/Concepts

**Application pool**
- in IIS represents an application process

**Reverse proxy**
- is the program that listens for HTTP requests from the internet and then makes requests to your app as though the request had come from the internet directly.
- is exposed directly to the internet , whereas the underlying web server is exposed only to the proxy.

**Runtime-dependent Deployments (RDD)**
- type of deployment that relies on the .NET Runtime being installed on the target machine (Windows, Linux, or macOS) that runs your published app.

**Self-contained Deployments (SCD)**
- type of deployment that contains all the code required to run your app, so the target machine doesn't need to have the .NET Runtime installed.
- the .NET Runtime will be package along with your app's code and libraries

## Commands

`dotnet publish`
- builds and packages everything your app needs to run

`dotnet <YourWebApp>.dll`
- the command that your server will run when running your application in production
- this is part of the **.NET Runtime** to run published applications


## How to deploy your ASP.NET Core application?
1. Publish first your application
    ```
    $ dotnet publish --output <directory> --configuration Release
    ```
