# Interoperability
- Interoperability enables you to preserve and take advantage of existing investments in unmanaged code. 
- Code that runs under the control of the common language runtime (CLR) is managed code, and code that runs outside the CLR is unmanaged code. 
- COM, COM+, C++ components, ActiveX components, and Microsoft Windows API are examples of unmanaged code.
- P/Invoke is a technology that allows you to access structs, callbacks, and functions in unmanaged libraries from your managed code.

#### Example
The following code example shows how to use the `DllImportAttribute` attribute to import the Win32 MessageBox function. The code example then calls the imported method.

```C#
using System;
using System.Runtime.InteropServices;

class Example
{
    // Use DllImport to import the Win32 MessageBox function.
    [DllImport("user32.dll", CharSet = CharSet.Unicode)]
    public static extern int MessageBox(IntPtr hWnd, String text, String caption, uint type);
    
    static void Main()
    {
        // Call the MessageBox function using platform invoke.
        MessageBox(new IntPtr(0), "Hello World!", "Hello Dialog", 0);
    }
}
```

## References
- [Interoperability Overview](https://learn.microsoft.com/en-us/dotnet/csharp/advanced-topics/interop/)
- [DllImportAttribute Class](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.interopservices.dllimportattribute?view=net-8.0)
- [Platform Invoke (P/Invoke)](https://learn.microsoft.com/en-us/dotnet/standard/native-interop/pinvoke)