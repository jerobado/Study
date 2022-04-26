# The `object` Type
- `object (System.Object)` is the ultimate base class for all types
- any type can be upcast to `object`
- `object` is a reference type, by virtue of being a class

For example:
```C#
// implmenenting a stack-like (last in, first out) data structure class
public
{
    int position;
    object[] data = new object[10];
    
    public void Push(object obj)
    {
        data[position++] = obj;
    }

    public object Pop()
    {
        return data[--position];
    }
}

// Usage
Stack stack = new Stack();
stack.Push("sakana");
string s = (string)stack.Pop();     // Downcast, so explicit cast is needed

Console.WriteLine(s);               // sakana
```

## Boxing & Unboxing
- _boxing_ is the act of converting a value-type instance to a reference-type instance
- the reference type can be either the `object` class or an interface

For example:
```C#
// Boxing
int x = 9;
object obj = x;         // Box the int

// Unboxing
int y = (int)obj;       // Unbox the int
```