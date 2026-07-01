# Open Close Principle (OCP)
- Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification

### Open to extension
- new behavior can be added in the future
- code that is closed to extension has fixed behavior

### Close to modification
- Changes to source or binary code are not required
- the only way to change the behavior of code that is closed to extension is to change the code itself

#### Tips
- solve the problem first using simple concrete code
- identify the kinds of changes the application is likey to continue needing
- modify code to be extensible along the axis of change you've identified

## References
- SOLID Principles for C# Developers by Steve Smith