# Type System

## Common Type System
- it supports the principle of inheritance
- each type in the Common Type System (CTS) is defined as either a _value type_ or a _reference type_
    - value types - can be defined using `struct` or `enum`; all built-in numeric types are `structs`
    - reference types - can be defined using the `class` or `record` keyword

**Reminders**

`class` - are use to model more complex behaviour, or data that is intended to be modiefied after a class object is create

`struct` - are best suited for small data structures that contain primarily data that isn't intended to be modified after thr struct is create

`record` - are for larger data structures that contain primarily data that isn't intended to be modified after the object is create

## Value Types
- type that directly contain their values, which means that the memeory is allocated inline in whatever context the variable is declared
- there is no separete heap allocation or garbage collection overhead for value-type variables

```C#
// Example
byte b = byte.MaxValue;
```
Using `struct`
```C#
public struct Coords
{
    public int x, y;

    public Coords(int point1, int point2)
    {
        x = point1;
        y = point2;
    }
}
```
Using `enum`
```C#
public enum FileMode
{
    CreateNew =1,
    Create = 2,
    Open = 3,
    OpenOrCreate = 4,
    Truncate = 5,
    Append  6,
}
```
## Reference Types
- a type that is defined using `class`, `record`, `delegate`, array, or `interface`
- the value of the declared variable using reference type is always `null` until you explicitly create an object by using the `new` operator, or assign it an object that has been created elsewhere by using `new`

```C#
// Example
Music song = new Music();
Music Song2 = song;
```
