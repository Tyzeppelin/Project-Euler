#include <stdio.h>
#include <stdlib.h>

#include "func.h"

int main()
{
    printf("5! --> %d", fact(5));


    int a = 10;
    int b = 1000000;

   //printf("\n %d elements pour attmeindre %d :%d * %d", a, b, interleave(b, a), fact(a-1));

    //int elem[3] = {0, 1, 2};

    //int *real = position(elem, 3, 3);

    //int trad = traduction(real, 3);

    int trad[] = {2, 0, 1 ,3};

    printf("\ntadam -> %d", traduction(trad, 4));


    //free(real);

    return 0;
}
