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

// Indices
var vowels = new char[] {'a', 'e', 'i', 'o', 'u'};
var lastElement = vowels[^1];    // 'u'
var secondToLast = vowels[^2];   // 'o'

// using Index type
Index first = 0;
Index last = ^1;
char firstElement = vowels [first]; // 'a'
char lastElement = vowels [last];   // 'u'

// Ranges
char[] firstTwo = vowels [..2]; // 'a', 'e'
char[] lastThree = vowels [2..]; // 'i', 'o', 'u'
char[] middleOne = vowels [2..3]; // 'i'

// using ^ symbol
char[] lastTwo = vowels [^2..]; // 'o', 'u'

// using Range type
Range firstTwoRange = 0..2;
char[] firstTwo = vowels [firstTwoRange]; // 'a', 'e'
```

