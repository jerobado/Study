**Stack**
- is a block of memory for storing local variables and parameters
- the stack logically grows and shrinks as a method or function is entered and exited

For example:
```C#
static int Factorial (int x)
{
    if (x == 0) return 1;
    return x * Factorial (x-1);
}
```

This recursive method will call itself. Each time the method is entered, a new `int` is allocated on the stack, and each time the method exits, the `int` is deallocated.

**Heap**
- is the memory in which objects (i.e., reference-type instances) resides
- created new objects is allocated on the heap, and a reference to that object is returned

For example:

We begin by creating a StringBuilder object referenced
by the variable ref1 and then write out its content. That StringBuilder object is
then immediately eligible for garbage collection because nothing subsequently uses
it.

Then, we create another StringBuilder referenced by variable ref2 and copy that
reference to ref3. Even though ref2 is not used after that point, ref3 keeps the
same StringBuilder object alive—ensuring that it doesn’t become eligible for col‐
lection until we’ve finished using ref3:

```C#
using System;
using System.Text;

StringBuilder ref1 = new StringBuilder ("object1");
Console.WriteLine (ref1);
// The StringBuilder referenced by ref1 is now eligible for GC.

StringBuilder ref2 = new StringBuilder ("object2");
StringBuilder ref3 = ref2;
// The StringBuilder referenced by ref2 is NOT yet eligible for GC.

Console.WriteLine (ref3); // object2
```