# .NET 7
- unification of .NET 5/6/7
- single software development kit (SDK) and base class library (BCL)

# Upgrading a .NET Core Project
- change the `TargetFramework` in your **.csproj** file to latest version

    ```csharp
    // old
    <PropertyGroup>
        <TargetFramework>net6.0</TargetFramework>
    </PropertyGroup>

    // new
    <PropertyGroup>
        <TargetFramework>net7.0</TargetFramework>
    </PropertyGroup>
    ```

- update version of dependencies that matches your .NET version

    ```csharp
    // old
    <ItemGroup>
        <PackageReference
            Include="Microsoft.AspNetCore.Identity.EntityFrameworkCore"
            Version="6.0.0" />
    </ItemGroup>

    // new
    <ItemGroup>
        <PackageReference
            Include="Microsoft.AspNetCore.Identity.EntityFrameworkCore"
            Version="7.0.0" />
    </ItemGroup>
    ```

- recent versions will be just configuration and minor API changes
- .NET Core 1.x will require more work
- .NET Framework will require a new project and substantial changes

# C# 11 New Features
- Generic math
- Auto-default structs
- Extended nameof scope
- Raw string literals

    ```csharp
    string message = """
        This is a very long string.
        It spans multiple lines.
            And there is even indentation.
                    Or "quotes" in there.

        Same like in Python's tripple quoted strings.
        """;
    
    string message2 = """This is valid message.""";

    // syntax errors
    string error1 = """Do not put something here.
        First line should be put here.
        """;
    
    string error2 = """
        Make sure your identation is consistent.
       This will fail because content is not properly aligned.
        Be careful.
        """;

    // raw string literals with string interpolation
    var location = $$"""
        GPS coordinates: {{{Longitude}}, {{Latitude}}}
        """;
    ```
- UTF-8 string literals
- List patterns
- File scoped types

    ```csharp
    // only useable within the file it's defined in
    file class LocalClass
    {
        public string SayHello()
        {
            return "Hello!";
        }
    }
    ```
- Generic attributes
- Newlines in string interpolation expression

# Resources
- [What's New in .NET 7](https://app.pluralsight.com/library/courses/dot-net-7-whats-new/table-of-contents)