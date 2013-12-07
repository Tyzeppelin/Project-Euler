#include <stdio.h>
#include <stdlib.h>

#include "func.h"

int main()
{


    int a = 10;
    int b = 1000000;

    int nb[3] = {0, 1, 2, 3};

   printf("Exemple pour [0, 1, 2, 3]\n");

    int n = interleave(13, 3);
    printf("du coup : %d", n);


    printf("4 elements, 13e pos --> %d", position(13, 4));


    //int elem[3] = {0, 1, 2};

    //int *real = position(elem, 3, 3);

    //int trad = traduction(real, 3);

    /*int trad[] = {2, 0, 1 ,3};

    printf("\ntadam -> %d", traduction(trad, 4));


    //free(real);*/

    return 0;
}
