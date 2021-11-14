# Strings
- C#'s string type represents an immutable (unmodifiable) sequence of Unicode characters
- a string literal is specified within double quotes:

    ```C#
    string message = "Atsui!";
    ```

- `string` is a reference type rathen than a value type. Its equality operators, however, follow value-type semantics

# Operations

### Concatenation
- the process of combining multple strings into one string

```C#
// the + operator concatenates two strings
string oxymoron = "Happy" + "Sad";

// one of the operands might be a non-string value
string agent = "00" + 7;    // 007
```

### Interpolation
- a string with the `$` character is called an _interpolated string_
- interpolated strings can include expressions enclosed in bracess
- any valid C# expression of any type can appear within the braces

```C#
string food = "pizza";
Console.Write($"I ate {food} yesterday.");  // I ate pizza yesterday.
```

### Comparison
- `string` does not support `<` and `>` operators for comparison
- you must use the string's `CompareTo` method
