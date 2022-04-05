# Iterations Statements
- C# has four (4) ways to do iterations or loops namely, `while`, `do-while`, `for` and `foreach` statements

## `while` loop

- `while` loop repeatedly executes a body of code while a `bool` expression is true
- the expression is tested _before_ the body of the loop is executed

For example:

```C#
int i = 0;
while (i < 3)
{
    Console.Write(i);
    i++;
}
```

## `do-while` loop

- expression is tested _after_ the loop body is executed

For example:

```C#
int i = 0;
do
{
    Console.WriteLine(i);
    i++;
}
while (i < 3);
```

## `for` loop
- are like `while` loop but with special clauses for _initialization_ and _iteration_ of a loop variable

For example:

```C#
// plain for-loop
for (int i = 0; i < 3; i++)
    Console.WriteLine(i);

// for-loop with multiple initialization variables
for (int i = 0; prevFib = 1, curFib = 1; i < 10; i++)
{
    Console.WriteLinen(prevFib);
    int newFib = prevFib + curFib;
    prevFib = curFib;
    curFib = newFib;
}

// removing the clauses will result into an infinite loop
for (;;)
    Console.WriteLine("infinite tsukuyomi");
```

## `foreach` loop
- iterates over each element in an enumerable object like an array and a string

For example:
```C#
foreach (char c in "noodles")
    Console.WriteLine(c);
```
