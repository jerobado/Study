# Interface Segregation Principle
- Clients should not be forced to depend on methods they do not use.

### Interface
- C# `interface` type/keyword 
- Public or accessible interface of a class
- whatever can be access by client code working with an instance of that type 

### Client
- is the code that is interacting with an instance of the interface
- it's the calling code


### ISP Violations
- large interfaces
- use of `NotImplementedException`
- code uses just a small subset of a larget interface