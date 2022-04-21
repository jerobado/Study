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

## Upcasting
- an _upcast_ operation creates a base class reference fom a subcass reference

For example:
```C#
Stock mpi = new Stock();
Asset a = mpi;              // Upcast

// a still references the same Stock object
Console.WriteLine(a == mpi);     // True

// a is of type Asset, even though it refers to an object of type Stock
Console.WriteLine(a.Name);          // Ok
Console.WriteLine(a.SharesOwned);   // Compie-time error
```

## Downcasting
- a _downcast_ operation creates a subclass reference from a base class reference
- if downcast fails, an `InvalidCastException` is thrown

For example:
```C#
Stock mpi = new Stock();
Asset a = mpi;                      // Upcast
Stock s = (Stock)a;                 // Downcast
Console.WriteLine(s.SharesOwned);   // <No error>
Console.WriteLine(s == a);          // True
Console.WriteLine(s == mpi);        // True
```

## `as` operator
- performs a downcast that evauates to `null` (rather than throwing an exception) if the downcast fails

For example:
```C#
Asset a = new Asset();
Stock s = a as Stock;       // s is nul, no exception thrown

// useful when you're going to test whether a type is nul
if (s != null)
    Console.WriteLine(s.SharesOwned);
```

## `is` operator
- tests whether a variable matches a _pattern_
- tests whether an object derives from a specified class (or implements an interface)

For example:
```C#
// test before downcasting
if (a is Stock)
    Console.WriteLine(((Stock)a).SharesOwned);

// introducing a variable while using 'is' operator
if (a is Stock s)
    Console.WriteLine(s.SharesOwned);

// the variable is available for immediate consumption
if (a is Stock s && s.SharesOwned > 10000000)
    Console.WriteLine("Wealthy");

// even if it remains outside scope of the 'is' expression
if (a is Stock s && s.SharesOwned > 10000000)
    Console.WriteLine("Wealthy");
Else
    s = new Stock();    // s is in scope

Console.WriteLine(s.SharesOwned);   // still in scope
```

# Virtual Function Members
- a function marked as `virtual` can be overridden by subclasses wanting to provide a specialized implementation
- methods, properties, indexers, and events can all be declared `virtual`

For example:
```C#
public class Asset
{
    public string Name;
    public virtual decimal Liability => 0;  // expression-bodied property
}

// use override modifer to override a virtual method
public class House : Asset
{
    public decimal Mortgage;
    public override decimal Liability => Mortgage;
}

// effect
House mansion = new House { Name="McMansion", Mortgage=250000 };
Asset a = mansion;
Console.WriteLine(mansion.Liability);       // 250000
Console.WriteLine(a.Liability);             // 250000
```

# Abstract Classes and Members
- a class declared as _abstract_ can never be instantiated. Only its concrete _subclasses_ can be instantiated
- abstract classes are able to define _abstract members_
- abstract members are like virtual members except that they don't provide a default implementation. That implementation must be provided by the subclass unless that subclass is also declared abstact

For example:
```C#
public abstract class Asset
{
    // Note empty implementation
    public abstract decimal NetValue { get; }
}

public class Stock : Asset
{
    public long SharesOwned;
    public decimal CurrentPrice;

    // Override like a virtual method
    public override decimal NetValue => CurrentPrice * SharesOwned;
}
```

## `base` keyword
- accessing an overridden function member from the subclass
- calling a base constructor

For example:
```C#
public class House : Asset
{
    ...
    public override decimal Liability => base.Liability + Mortgage
}

// calling a base constructor
public class Baseclass
{
    public int X;
    public Baseclass() { }
    public Baseclass(int x) { this.X = x } // we want to use this in Subclass
}

public class Subclass : Baseclass
{
    public Subclass(int x) : base(x) { } // we do it like this
}
```