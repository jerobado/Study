`Enum`
---
- is a special value type that lets your specify a group of named numeric constants

For example
```C#
public enum BorderSide
{
    Left,
    Right,
    Top,
    Bottom
}

// assigning with default values
public enum BordeSide
{
    Left = 1,
    Right = 2,
    Top = 3,
    Bottom = 4
}

// with explicit integral type
public enum BordeSide : byte
{
    Left = 1,
    Right = 2,
    Top = 3,
    Bottom = 4
}
```
