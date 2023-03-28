# Factory Method
- also known as _Virtual Contructor_
- the intent of the factory method is to define an interface for creating an object, but to let subclasses decide which class to instantiate
- factory method lets a class defer instantiation to subclasses

### Use Cases
- when a class can't anticipate the class of objecxts it must create
- when a class want's subclasses to specify the objects it create
- when classes delegate responsibility to one of several helper subclasses, and you want to localizet he knowledge of which helper subclass is the delegate
- as a way to enable reusing of existing objects


# Resources
- [Factory Method](https://refactoring.guru/design-patterns/factory-method)