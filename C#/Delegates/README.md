# Delegates
- a delegate is an object that knows how to call a method


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
Transformer t = SomeMethod;     // create a delegate instance

// invoke
d("Just learned C# delegate!");
// or (points to SomeMethod)
d.Invoke("Invoke the method we are pointing to");



// Another example (shorthand version)
delegate int Transformer(int x);
int Square(int x) => x * x;
Transformer t = Square;
int answer = t(3)           // answer is 9
```


# Resources
- C# in a Nutshell