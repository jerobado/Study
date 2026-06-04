## .NET

Value types vs reference types

Difference between `IEnumerable` and `IQueryable`

Abstract class vs Interface

## C#

`async` vs `await`
- async marks a method as asynchronous
- awaits pauses execution until a task completes
- async methods can be sequential or parallel
What is `CancellationToken`
- is a signalling mechanis that let's you cancel long running or asynchronous tasks gracefully without killing threads

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