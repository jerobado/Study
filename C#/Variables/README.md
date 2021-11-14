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