# Classes
- a _class_ is the most common kind of reference types

```C#
class Magic { }
```

## Fields
- a _field_ is a variable that is a member of a class or struct

```C#
class Magic 
{
    string description;
    public int damage = 10;
}
```

## Field modifiers
- field modifiers are keywords use to declare how field will be access

### `readonly`
- `readonly` modifier prevents a field from being modified after construction
- a read-only field can be assigned only in its declaration or within the enclosing type's constructor

```C#
public class SamplePoint
{
    public int x;
    // Initialize a readonly field
    public readonly int y = 25;
    public readonly int z;

    public SamplePoint()
    {
        // Initialize a readonly instance field
        z = 24;
    }

    public SamplePoint(int p1, int p2, int p3)
    {
        x = p1;
        y = p2;
        z = p3;
    }

    public static void Main()
    {
        SamplePoint p1 = new SamplePoint(11, 21, 32);   // OK
        Console.WriteLine($"p1: x={p1.x}, y={p1.y}, z={p1.z}");
        SamplePoint p2 = new SamplePoint();
        p2.x = 55;   // OK
        Console.WriteLine($"p2: x={p2.x}, y={p2.y}, z={p2.z}");
    }
    /*
     Output:
        p1: x=11, y=21, z=32
        p2: x=55, y=25, z=24
    */
}
```

## Properties
- are like field but they contain logic like methods
- a property is declared like a field but with a `get`/`set` block added

For example:
```C#
public class Stock
{
    decimal currentPrice;           // The private "backing" field
    public decimal CurrentPrice     // The public property
    {
        get { return currentPrice; }
        set { currentPrice = value; }
    }
}

// similar syntax
public decimal Worth
{
    get => currentPrice * sharedOwned;
    set => sharedOwned = value / currentPrice;
}

// automatic properties
public class Stock
{
    ...
    public decimal CurrentPrice { get; set; }
}

// property initializers
public decimal CurrentPrice { get; set; } = 999;
```

## Methods
- a _method_ performs an action in a series of statements
- can receive _input_ data from the caller by specifying _parameters_ and _output_ data back to the caller by specifying a _return type_
- a method can specify a `void` return type, indicating that it doesn't return any value to its caller
- a method can also output data back to the caller via `ref`/`out` parameters

# Partial Types ad Methods
- allow a type definition to be split--typically across multiple files
- all the parts must use the `partial` keyword
- all the parts must have the same accessibility, such as `public`, `private`, and so on

For example:
```C#
public partial class Employee
{
    public void DoWork()
    {
    }
}

public partial class Employee
{
    public void GoToLunch()
    {
    }
}

// result at compile time
pubilc class Employee
{
    public void DoWork()
    {
    }

    publilc void GoToLunch()
    {
    }
}
```

