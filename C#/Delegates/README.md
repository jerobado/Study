# Delegates

Example:
```C#
void SomeMethod(string text)
{
    Console.WriteLine(text);
}

// declare
public delegate void MyDelegate(string text);

// instantiate
// you use the method as an argument to the delegate
MyDelegate d = new MyDelegate(SomeMethod);		

// invoke
d("Just learned C# delegate!");
// or (points to SomeMethod)
d.Invoke("Invoke the method we are pointing to");
```
