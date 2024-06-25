# Collections

`HashSet<T>`
- elements are not in ordered
- implemented with a hashtable that stores just keys

Example
```C#
var letters = new HashSet<char>("the quick brown fox");

Console.WriteLine(letters.Contains('t'));       // true
Console.WriteLine(letters.Contains('j'));       // false

foreach (char c in letters) Console.Write(c)    // the quickbrownfx
```

`SortedSet<T>`
- elements are ordered


# Resources
- C# in a Nutshell by Joseph Albahari