`switch` expression
---
- evaluate a  single expression from a list of candidate expression based on a pattern match with an input expression

For example:
```C#
int index = 1;
var today = index switch
{
    1 => "Monday",
    2 => "Tuesday",
    3 => "Wednesday",
    4 => "Thursday",
    5 => "Friday",
    6 => "Saturday",
    7 => "Sunday"
    _ => "Unknown"
};

Console.WriteLine(today);   // Output: Monday
```
