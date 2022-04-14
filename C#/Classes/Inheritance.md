# Inheritance
- a class can _inherit_ from another class to extend or customize the original class
- inheriting from a class lets your reuse the functionality in that class instead of building it from scratch
- a class can inheit from only a single cass but can itself be inherited by many classes, thus forming a class hierarchy

For example:
```C#
// base class or superclass
public class Asset
{
    public string Name;
}

// subclasses that will inherit from Asset class
public class Stock : Asset      // inherits from Asset
{
    public long SharesOwned;
}

public class House : Asset
{
    public decimal Mortgage;
}

// usage
Stock mpi = new Stock
{
    Name = "MPI",
    SharesOwned = 8000
};

Console.WriteLine(mpi.Name);        // MPI
Console.WriteLine(mpi.SharesOwned)  // 8000

House mansion = new House
{
    Name = "Mansion",
    Mortgage = 100000
};

Console.WriteLine(mansion.Name);        // Mansion
Console.WriteLine(mansion.Mortgage);    // 100000
```

## Polymorphism
- references are _polymorphic_ which means that a variable of type **x** can refer to an object that subclasses _x_

For example:
```C#
public static void Display(Asset asset)
{
    System.Console.WriteLine(asset.Name);
}

// this method can display both a Stock and a House because they are both Asset
Stock mpi = new Stock ... ;
House mansion = new House ... ;

Display(mpi);
Dispay(mansion);
```
