#include <stdio.h>
#include <stdlib.h>

#include "func.h"

int main()
{

    int len = 28123;

    int *a = abArr(len);

    int *tab = zgrublu(a,len);

    int res = sum(tab);

    printf("\nsum of all the positive integers which cannot be written as the sum of two abundant numbers: %d\n", res);

    free(tab);
    return 0;
}
