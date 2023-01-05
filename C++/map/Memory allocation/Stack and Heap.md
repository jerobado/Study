# Stack and Heap Memory

## Stack
- memory is allocated in the stack when:
    - a function is called
    - a local variable is declared
- **allocation and deallocation for stack memory is automatically done**

For example:
```C++
int hello()
{
    int a = 100;
    return a;
}

int main()
{
    int a;
    int b = -3;
    int c = 123;
    int *p = &b;
    int d = hello();
    return 0;
}
```

## Heap
- memory is allocated in the heap when:
    - using the `new` operator followed by the constructor
    - using `new []`
    - using `malloc()`
- to free memory in the heap:
    - use `delete` for objects created with `new`
    - use `delete []` for array of objects created with `new []`
    - use `free()` function
- **allocated explicitly by programmers and <ins>it won't be deallocated until it is explicitly freed</ins>**

# Resources
- [Stack and Heap Memory](https://courses.engr.illinois.edu/cs225/fa2022/resources/stack-heap/)