# Jump statements
- C# jump statements are `break`, `continue`, `goto`, `return` and `throw`

## `break`
- ends the execution of the body of an iteration or `switch` statement

For example:
```C#
int x = 0;
while (true)
{
    if (x++ > 5)
        break;      // break from the while loop
}
// execution continues here after break
...
```

## `continue`
- forgoes the remaining statements in a loop and makes an early start on the next iteration

For example:
```C#
for (int i = 0; i < 10; i++)
{
    if ((i % 2) == 0)       // check if i is even
        continue;           // jumps to next iteration
    
    Console.Write(i + " ");
}
// Output: 1 3 5 7 9
```

## `goto`
- transfer execution to another label within a statement block

For example:
```C#
int i = 1;
startLoop:
if (i <= 5)
{
    Console.Write(i + " ");
    i++;
    goto startLoop;
}
// Output: 1 2 3 4 5
```

## `return`
- exits the method and must return an expression of the method's return type if the method is non-void

For example:
```C#
decimal AsPercentage(decimal d)
{
    decimal p = d * 100m;
    return p;
}
```

## `throw`
- throws an exception to indicate an error has occured

For example:
```C#
if (w == null)
    throw new ArgumentNullException (...);
```





