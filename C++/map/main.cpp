#include <stdio.h>
#include <map>

using namespace std;


int main()
{
    // Create an <int, char> map
    map<int, char> ASCII {
        {65, 'A'},
        {66, 'B'},
        {67, 'C'}
    };

    // Choose a key
    printf("ASCII: %c\n", ASCII[65]);

    // printf can also do that!! #wtf
    printf("ASCII: %c # using printf\n", 94);

    return 0;
}
