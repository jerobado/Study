# Domain-driven Design (DDD)
- is an approach to software development that centers the development on programming a domain model that has a rich understanding of the processes and rules of a domain
- is a software design philosophy that focuses on understanding domain experts and building the software as a model of its domain
- the structure and language of software code (class names, class methods, class variables) should match the business domain. For example, if a software processes loan applications, it might have classes such as `LoanApplication` and `Customer`, and methods such as `AcceptOffer` and `Withdraw`. 
- organize the code so it is aligned to the business problems, and using the same business terms (ubiquitous language)

# Concepts



**Command Query Responsibility Segregation (CQRS)**
- is an architectural pattern for separating reading data (a 'query') from writing to data (a 'command')

**context**
- the setting in which a word or statement appears that determines its meaning

**bounded context**
- the boundary of properties or behaviour or a particular domain model

**context mapping**
- th eprocess of identifying bounded context and their relationships to one another

**domain**
- the subject area to which the user applies a program is the domain of the so

**domain model**
- a system of abstraction that describes selected aspects of a domain and can be used to solve problems related to that domain

**entity**
- is an object not defined by its attributes, but its identity
- e.g., most airlines assign a unique number to seats on every flight: this is the seat's identity. 

**repository**
- is an object with methods for retrieving domain objects from a data store (e.g., a database)

**service**
- refers to a software functionality or a set of software functionalities (such as the retrieval of specified information or the execution of a set of operations) with a purpose that different clients can reuse for different purposes

**ubiquitous language**
- the domain model should form a _common language_ shared by domain experts for describing system requirements, business uers, sponsors and developers
- use domain terminology everywhere; make it ubiquitous

**value object**
- is an immutable object that contains attributes but has no conceptual identity
- e.g., when people exchange business cards, for instance, they only care about the information on the card (its attributes) rather than trying to distinguish between each unique card 

**data transfer object (DTO)**
- is a class representing some data with no logic in it
- are usually used for transferring data between different applications or different layers within a single application
- you can look at them as dumb bags of information the sole purpose of which is to just get this information to a recipient
- An object that carries data between processes in order to reduce the number of method calls.

# Layers

**Domain layer**
- responsible for representing concepts of the business, information about the business situation, and business rules
- the heart of the business software
- must be implemented in Plain Old CLR Objects (POCO)
- should have no dependencies to other layers

**Application layer**
- defines the jobs that software is supposed to do and directs the expressive domain objects to work out problems
- it is a thin layer
- it does not contain business rules or knowledge, but only coordinates tasks and delegates work to collaborations of domain objects in the next layer down
- it does not have state reflecting the business situation, but it can have state that reflects the progress of a task for the user or the program
- includes use cases, commands, queries, and their respective handlers, focusing on coordinating tasks and delegating work to the domain and infrastructure layers
- serves as the bridge between the domain layer and the outer layers of the system, such as the user interface or external services.
- it’s responsible for implementing use cases, coordinating tasks, and handling cross-cutting concerns like validation and authorization.


**Infrastructure layer**
- is how tht e data that is initially hel in domain entities (in memory) is persisted in databases or another persistent store

**<ins>REMEMBER</ins>**
- Application layer depends on Domain and Infrastructure
- Infrastructure depends on Domain
- **Domain doesn't depend on any layer**

# Resource(s)
- [Domain Driven Design by Martin Fowler](https://martinfowler.com/bliki/DomainDrivenDesign.html)
- [Domain-driven design via Wikipedia](https://en.wikipedia.org/wiki/Domain-driven_design)
- [Get your feet wet with domain-driven design: 3 guiding principles](https://techbeacon.com/app-dev-testing/get-your-feet-wet-domain-driven-design-3-guiding-principles)
- [Design a DDD-oriented microservice](https://docs.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/ddd-oriented-microservice)
- [Implementing Domain-Driven Design in C#: Patterns and Practices](https://www.w3computing.com/articles/implementing-domain-driven-design-csharp-patterns-practices/)
- [DTO vs Value Object vs POCO](https://enterprisecraftsmanship.com/posts/dto-vs-value-object-vs-poco/)
- [Data Transfer Object](https://martinfowler.com/eaaCatalog/dataTransferObject.html)