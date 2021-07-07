#include <iostream>
#include <stdio.h>
#include <map>
#include <unordered_map>


using namespace std;


int main()
{
    // Create an <int, char> map
    map<int, char> ASCII {
        {65, 'A'},
        {66, 'B'},
        {67, 'C'}
    };

    unordered_map<int, char> ASCII_UNORDERED {
        {65, 'A'},
        {66, 'B'},
        {67, 'C'}
    };

    // Choose a key
    printf("ASCII: %c\n", ASCII[65]);

    // printf can also do that!! #wtf
    // printf("ASCII: %c # using printf\n", 94);
 
    // display ASCII
    cout << "// display ASCII" << endl;
    for (auto iter = ASCII.begin(); iter != ASCII.end(); iter++)
    {
        cout << iter->first << ": " << iter->second << endl;
    }

    // display ASCII_UNORDERED
    printf("// display ASCII_UNORDERED\n");
    for (auto iter = ASCII_UNORDERED.begin(); iter != ASCII_UNORDERED.end(); iter++)
    {
        printf("%d: %c\n", iter->first, iter->second);
    }
   
    return 0;
}
