# Azure Service Bus
- is a fully managed enterprise message broker with message queues and publish-subscribe topics

### Features and Benefits
- decouple applications and services from each other

### Terms

**messages** - a container decorated with metadata, and contains data. Data can be any kind of information, including structured data encoded with the common formats such as the following ones: JSON, XML, Apache Avro, Plain Text.

### Concepts

**Queues**
- 1 sender, 1 receiver
- messagges are sent to and received from queues
- queues store messages until the receiving application is available to receive and process them
- messages in queues are ordered and timestamped on arrival
- used for point-to-point communication

**Topics**
- 1 sender, multiple receivers


## References
- [What is Azure Service Bus?](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview)