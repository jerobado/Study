Asynchronous programming
----

**`await`**
- the `await` keyword will pause execution of the method until a result is available, without blocking the calling (UI) thread


### Reminders
- always `await` asynchronous method
- don't use `async void` as method signatures, only use it for **event handlers** or **delegate**
- using `async` and `await` in ASP.NET means the web server can handle other requests