# Session
- is an environment in which PowerShell runs
- a new session is created for you each time you start PowerShell

### PSSessions or PowerShell sessions
- are user-managed sessions on the local computer or on a remote computer
- PSSession remains available until you delete it or it times out

### Why Use a PSSession
- you need a persistent connection to a remote computer
- you can run a series of commands that share data, such as the value of variables, the contents of a function, or the definition of an alias

#  How to Create a PSSession
To create a PSSession, use the `New-PSSession` cmdlet. To create the PSSession on a remote computer, use the **ComputerName** parameter of the `New-PSSession` cmdlet
```powershell
New-PSSession -ComputerName ServerA
```
This will create the PSSession and returns an object that represent the PSSession. You can save the object in a variable when you create the PSSession, or you can use a `Get-PSSession` command to get the PSSession at a later time.

For example, saving the PSSession in a variable:
```powershell
$ps = New-PSSession -ComputerName ServerA
```

# How to Create PSSessions on Multiple Computers
To create PSSessions on multiple computers, use the **ComputerName** parameter of the `New-PSSession` cmdlet. Type the names of the remote computers in a comma-separated list

```powershell
New-PSSession -ComputerName ServerA, ServerB, ServerC
```


# Resources
- [about PSSessions](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_pssessions?view=powershell-7.3)