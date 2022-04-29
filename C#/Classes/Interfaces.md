# Interfaces
- similar to a class, but only _specifies behaviour_ and does not hold stat (data)
- can define only functions and not fields
- implicitly abstract
- can contain only functions, that is, methods, properties, events and indexers

For example:
```C#
public interface IEnumerator
{
    bool MoveNext();
    object Current { get; }
    void Reset();
}
```