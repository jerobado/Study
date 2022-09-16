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

Console.WriteLine(today);   // Monday

// switching on multiple values (tuple pattern)
(int cardNumber, string suite) = 12, "spades"
string cardName = (cardNumber, suite) switch
{
    (12, "spades") => "King of spades",
    (13, "clubs") => "King of clubs"
};

Console.WriteLine(cardName); // King of spades
```

If you omit the default "`_`" expression and the switch fails to match, an exception is thrown.

## Exceptions

Duplicate pattern
```C#
int index = 1;
var today = index switch
{
    1 => "Monday",
    1 => "Tuesday",     // should not have a duplicate pattern
    _ => "Unknown"
};
```

`SwitchExpressionException`
```C#
int index = 7;          // no match because we omit the default (_) expression 
var today = index switch
{
    1 => "Monday",
    2 => "Tuesday"
};
```