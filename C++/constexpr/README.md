# `constepr`
- The keyword `constexpr` was introduced in C++11 and improved in C++14. It means _constant expression_.
- `constexpr` indicates that the value, or return value, is constant and, where possible, is computed at compile time.

### Example
```C++
constexpr float x = 42.0;
constexpr float y{108};
constexpr float z = exp(5, 3);
constexpr int i; // Error! Not initialized
int j = 0;
constexpr int k = j + 1; //Error! j not a constant expression
```

### References
- [constexpr (C++) | Microsoft Learn](https://learn.microsoft.com/en-us/cpp/cpp/constexpr-cpp?view=msvc-170)