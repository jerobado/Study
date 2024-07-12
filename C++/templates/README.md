# Templates
- A template is a construct that generates an ordinary type or function at compile time based on arguments the user supplies for the template parameters.

Example
```c++
template <typename T>
T minimum(const T& lhs, const T& rhs)
{
    return lhs < rhs ? lhs : rhs;
}
```

###
- [Templates (C++)](https://learn.microsoft.com/en-us/cpp/cpp/templates-cpp?view=msvc-170)