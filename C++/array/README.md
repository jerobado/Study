# Array
- in C++, an array is a variable that can store multiple values of the same type.


### Example

C-style array
```c
// declaration
int solar_system[8];

// declare and initialize
int x[6] = {19, 10, 8, 17, 9, 15};
```

C++ style
```c++
#include <array>

// declaration
std::array<int, 5> numbers; // type and number of arrays

// initialization
std::array<int, 5> numbers = {1, 2, 3, 4, 5};   // initializer list
std::array<int, 5> basket {1, 2, 3, 4, 5};   // uniform initialization
```

### References
- [C++ Arrays](https://www.programiz.com/cpp-programming/arrays)
- [C++ std::array](https://www.programiz.com/cpp-programming/std-array)