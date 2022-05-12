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

## Extending an Interface
- interfaces can derive from other interfaces

For example:
```C#
public interface IUndoable             { void Undo(); }
public interface IRedoable : IUndoable { void Redo(); }
```
