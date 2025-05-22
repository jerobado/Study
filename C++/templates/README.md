# Templates
- A template is a construct that generates an ordinary type or function at compile time based on arguments the user supplies for the template parameters.

Example
```c++
// this is called a function template
template <typename T>
T minimum(const T& left, const T& right)
{
    return left < right ? left: right;
}

int a = minimum<int>(3, 9); // return 3

// let the compiler determine the type base on the arguments
int b = minimum(0.34, 0.7) ;
```

###
- [Templates (C++)](https://learn.microsoft.com/en-us/cpp/cpp/templates-cpp?view=msvc-170)