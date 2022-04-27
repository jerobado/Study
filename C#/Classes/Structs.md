# Structs
- a struct is a value type, whereas a class is a reference type
- a struct does not support inheritance

For example:
```C#
public struct Point
{
    int x, y;
    public Point(int x, int y)
    {
        this.x = x;
        this.y = y;
    }
}

// Usage
Point p1 = new Point();         // p1.x and p1.y will be 0
Point p2 = new Point(1, 1);     // p2.x and p2.y will be 1
```