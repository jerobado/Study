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

