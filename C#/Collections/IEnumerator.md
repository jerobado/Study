# IEnumerator and IEnumerable
- is an interface that defines the basic low-level protocol by which elements in a collection are traveresed -- or enumerated -- in a forward-only manner

```C#
// IEnumerator declaration
public interface IEnumerator
{
    bool MoveNext();
    obect Current { get; }
    void Reset();
}
```

`MoveNext()` - advances the current element of "cursor" to the next position, returning `false` if there are no more elements in the collection.

`Current` - returns the element at the current position.

`Reset()` - if implemented, moves back to the start, allowing the collection to be enumerated again.

Collections do not usually _implement_ enumerators; instead, they _provide_ enumerators, via the interface `IEnumerable`:

```C#
public interface IEnumerable
{
    IEnumerator GetEnumerable();
}
```

The following example illustrates low-level use of `IEnumerable` and `IEnumerator`:
```C#
string s = "Hello";

// Because string implements IEnumerable, we can call GetEnumerator():
IEnumerator rator = s.GetEnumerator();

while (rator.MoveNext())
{
char c = (char) rator.Current;
Console.Write (c + ".");
}

// Output: H.e.l.l.o.
```

Use `foreach` instead of calling enumerators directly
```C#
string s = "Hello"; // The String class implements IEnumerable

foreach (char c in s)
Console.Write (c + ".");

// Output: H.e.l.l.o.
```

# IEnumerable&lt;T> and IEnumerator&lt;T>
IEnumerator and IEnumerable are nearly always implemented in conjunction with
their extended generic versions:
```C#
public interface IEnumerator<T> : IEnumerator, IDisposable
{
    T Current { get; }
}

public interface IEnumerable<T> : IEnumerable
{
    IEnumerator<T> GetEnumerator();
}
```