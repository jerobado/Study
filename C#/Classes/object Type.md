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
