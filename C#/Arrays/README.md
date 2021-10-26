# Arrays
- an array represents a fixed number of variables called _elements_ of a particular type
- the elements in an array are always stored in a contiguous block of memory, providing highly efficient access

### Syntax and Usage
```C#
// Declare an array of 5 characters
char[] vowels = new char[5];

// Assigning and acessing an element in an array
vowels[0] = 'a';
vowels[1] = 'e';
vowels[2] = 'i';
vowels[3] = 'o';
vowels[4] = 'u';
Console.WriteLine(vowels[1]); // prints 'e'

// Initialization
int[] a = new int[100];
Console.Write(a[78]);  // prints 0
```

