#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("Hello world!\n");

    int i;

    for (i = 1; i < 20; i++)
        printf("\n 1/%d, %.20lf", i, (double)1/i);


    return 0;
}
