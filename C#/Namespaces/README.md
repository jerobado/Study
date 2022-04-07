# Namespaces
- is a domain for type names
- namespaces are independent of assemblies, which are `.dll` files that serve as units of deployment
- types not defined in any namespaces are said to reside in the _global namespace_

For example:
```C#
namespace Outer.Middle.Inner
{
    class Class1 {}
    class Class2 {}
}

// same as above
namespace Outer
{
    namespace Middle
    {
        namespace Inner
        {
            class Class1 {}
            class Class2 {}
        }
    }
}
```

## `using` directive
- allows you to _import_ a namespace

```C#
using Outer.Middle.Inner;

Class1 = c;
```

## `using static` directive
- imports a _type_ including fields, properties and nested types rather than a namespace
- all static members of the imported type can then be used without qualification

```C#
using static System.Console;

WriteLine("Ola!");

// can be also applied to enum types
using static System.Windows.Visibility;     // we can use Hidden

var textBox = new TextBox { Visibility = Hidden };
```

## Repeated namespace
- you can repeat a namespace declration, as long as the type names within the namespaces don't conflict:

```C#
namespace Outer.Middle.Inner
{
    class Class1 { }
}

namespace Outer.Middle.Inner
{
    class Class2 { }
}
```

## Aliasing Types and Namespaces

```C#
using PropertyInfo2 = System.Reflection.PropertyInfo;
class Program { PropertyInfo2 p; }

// aliasing an entire namespace
using R = System.Reflection;
class Program { R.PropertyInfo p; }
```