## .NET

### Value types vs Reference types

Value types
- value types store their data directly in memory
- primitive types like `int`, `float`, `char`, `bool`, `struct`, and `enum` 
- when assigned to a new variable, a copy of the value is made
- modifying one variable does not affect the original

Reference types
- store a reference (memory address) to memory instead of storing the value directly
- when assigned to a new variable, both variables point to the same memory location, meaning changes to one object affect the other
- example are `class`, arrays

Difference between `IEnumerable` and `IQueryable`

### Abstract class vs Interface

Interface
- defines a contract that a class must follow
- contains method signatgures only (no implementations)
- a class can have multiple interfaces

Abstract class
- can have abstract methods (no implementation) and concrete methods (with implementation)
- allows related classes to shared code
- a class can inherit only one abstract class


Compilation process
- C# code is translateed to Common Intermediate Language (CIL)
- CIL is executed by the Common Language Runtime (CLR)

## C#

`async` vs `await`
- async marks a method as asynchronous
- awaits pauses execution until a task completes
- async methods can be sequential or parallel
What is `CancellationToken`
- is a signalling mechanis that let's you cancel long running or asynchronous tasks gracefully without killing threads

Delegate
- is a type that represents a referenced to a method
- it allows method to be passed as arguments
- ideal for event handling, callbacks, and functinoal programming

`func<T>`
- returns a value
- `Func<int, int, int> add = (x, y) => x + y`

`Action<T>`
- returns void
- takes parameters
- `Action<string> print = Console.WriteLine`

`Predicate<T>`
- returns a bool
- `Predicate<int> isEven = x => x % 2 == 0`


## Design Patterns

What is SOLID?
- **Single Responsibility** - a class should only have one specific job or responsiblity
- **Open/Closed** - you should be able to add new functionality withtout altering existing, tested code
- **Liskov Substitution** - objects of a subclass should behave in a way that they can replace objects of their parent class without breaking the application
- **Interface Segragation** - create atomic interfaces
- **Dependency Injection** - high-level modules should not depend on low level modules, should depend on abstraction

What is Dependency Injection?
- is a design pattern for achieving Inversion of Control (IoC) principle
- it's the process of "injecting" objects via interface in a class without the class directly implementing it
- benefit is loose coupling between two objects


## OOP

What are the pillars of OOP
- Encapsulation, Abstraction, Inheritance and Polymorphism
- _Encapsulation_ is the process of bundling properties and methods to work on a data into a single unit called a class
- _Abstraction_ is the process of showing only the essential features of an object while hiding complext background iplementations
- _Inheritance_ allows a class (child) to inherit or acquire the properties and methods of an existing class (parent)
- Polymorphism allows a method in a class to behave differently via method overloading or overriding


## References
- [.NET Interview Questions and Answers (With Code Examples)](https://zerotomastery.io/blog/dot-NET-interview-questions/)