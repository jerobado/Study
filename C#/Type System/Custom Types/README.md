# Custom Types

The following types can be use to create custom types:
- `struct`
- `class`
- `interface`
- `enum`
- `record`

## Interfaces
- define behaviour for multiple types
- an interface may NOT declare instance data such as field, auto-implemented properties, or property-like events
- by using interfaces, you can, for example, include behavviour from multiple sources in a class. That capability is important in C# because the language doesn't support multiple inheritance of classes.
- you must use an interface if you want to simulate inheritance for structs, becuase they can't actually inherit from another struct or class.

To create an interface type:
```C#
// By convention, interfaces should begin with the letter 'I'
interface IEquatable<T> 
{
    bool Equals(T obj);
}
```
**Reminders**
- any class or struct that wants to implement the interface above must contain a definition for an `Equals` method that matches the signature that the interface specifies
- a class or struct can implement multiple interfaces, but a class can only inherit from a single class
- interfaces **CAN** contain instance <ins>methods</ins>, <ins>properties</ins>, <ins>events</ins>, <ins>indexers</ins>, or any combination of those four member types
- interfaces **MAY** contain <ins>static constructors</ins>, <ins>field</ins>, <ins>constants</ins>, or <ins>operators</ins>
- interfaces **CAN'T** contain <ins>instance field</ins>, <ins>instance constructors</ins>, or <ins>finalizers</ins>

