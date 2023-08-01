# App Offline file (`app_offline.html`)
- the App Offline file is used by the ASP.NET Core Module to shutdown an app

## How it works

If a file with the name `app_offline.htm` is detected in the root directory of an app, the ASP.NET Core Module attempts to gracefully shut down the app and stop processing incoming requests. If the app is still running after the number of seconds defined in shutdownTimeLimit, the ASP.NET Core Module stops the running process.

While the `app_offline.htm` file is present, the ASP.NET Core Module responds to requests by sending back the contents of the `app_offline.htm` file. The `app_offline.htm` must be less than 4 GB. When the `app_offline.htm` file is removed, the next request starts the app.

Reminders
- Files can also be unlocked by manually stopping the app pool in the IIS Manager on the server. Don't use the `app_offline.htm` file when using the IIS Manager to stop and restart the app pool.

# Resources
- [App Offline file (app_offline.htm)](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/app-offline?view=aspnetcore-7.0)