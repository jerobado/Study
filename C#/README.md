# C#
_C#_ is a modern, object-oriented, and type-safe programming language.


# Definition of terms/concepts

**Assembly**
- is the unit of packaging and deployment in .NET
- can be an _application_ or a _library_

**Namespace**
- grouping of .NET types

**Expressions**
```C#
// Example
12 * 30;
```

**Importing**
- to import a namespace with the `using` directive
```C#
// Example
using System;
```

**Identifiers**
- are names that programmers choose for their classes, method, variables and so on.
- made up of Unicode characters starting with a letter or underscore
- case sensitive
```C#
// Example
System x Console WriteLine
```

**Keywords**
- are names that mean something special to the compiler
- most of them are reserved, which means you can't use them as identifiers
- you can use them by adding the prefix `@`, i.e. `@foreach`
- [List of C# keywords](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/)


**Method**
- can receive _input_ data from the caller by specifying _parameters_ and _output_ data back to the caller by specifying a _return type_
```C#
using System;

Console.WriteLine(FeetToInches(37);     // 37 is the argument

int FeetToInches(int feet)              // int feet is a parameter
...
```

**Statements**
```C#
// Example
int x = 12 * 30;
System.console.WriteLine(x);
```

**Statement block**
- series of statements surrounded by a pair of braces
```C#
// Example
{
    int x = 12 * 30;
    System.Console.WriteLine(x);
}
```