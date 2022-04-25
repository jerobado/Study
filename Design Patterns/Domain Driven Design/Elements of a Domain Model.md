# Elements of a Domain Model

**Domain**
- is the hear of business software
- focus on behaviours not attributes

**Anemic Domain Model**
- model with <ins>**classes focused on state management**</ins>
- good for CRUD

**Rich Domain Model**
- model with <ins>**logic focused on behaviour, not just state**</ins>
- preferred for DDD

**Entity**
- a mutable class with an identity (not tied to its property values) used for tracking and persistence
- what can happen
- when it can happen
- what conditions dictate when it can do that thing
- tables names corresponding to your domain models
- something that needs to be tracked over time and whose attributes are likely to change over time
- e.g., Users, Movies, Student, Transactions, etc.

**Value Objects**
- an immutable class whose idenity is dependent on the combination of its values
- measures, quantifies, or describes a thing in the domain
- identity is based on composition of values
- immutable
- no side effects
- good place to put methods and logics
- the state of a value object should not be changed once it has been created
- e.g., String, Date, Money

**Service**
- provide a place in the model to hold behaviour that doesn't belong elsewhere in the domain
- not a natural part of an entity or value object
- has an interface defined in terms of other domain model elements
- stateless, but may have side effects
= live in the core (domain) of the application
- e.g., UI and App, Domain, Infrastructure

**Aggregates**
- consist of one or more entities or value objects that change together
- should enforce data consistency
- is a cluster of associated objects that we treat as a unit for the purpose of data changes

**Aggregate Root**
- the entry point of an aggregate which ensures the integrity of the entire graph

**Repository**
- managed the life cycle of the persisted objects
- represents all objects of a certain type as a conceptual set like a collection with more elaborate queryihng capability
- an abstraction your domain model uses to define what persistence needs it has
- a class the encapsulates the data persistence for an aggregate root

**Domain Events**
- a class that captures the occurence of an event in a domain object
- alert that some activity occured or some state changed in teh context
- other domain can subscribe to the "news"
- can communicate outside of the domain
- encapsulated as objects
- each event is a full-fledge class
- e.g., AppointmentScheduled, AppointmentConfirmed, ClientRegistered, etc.
- create events as needed, not just in case