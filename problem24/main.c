#include <stdio.h>
#include <stdlib.h>

#include "func.h"

int main()
{


    printf("c'est tres sale --> ");
    int *s = sale(1000000);
    printArr(s, 10);

/*
    int len = 10;
    int reach = 1000000;
    int nb[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};


    printf("Resolution pour [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n");
    printf("\n On cherche le 1000000!\n\n");

    long unsigned int vit = position(reach, len);

    printf("\n Position dans le tableau d'int --> %lu", vit);

    long int ban = traduction(nb, 10, vit);

    printf("\ntrad de %lu dans un e arr de 10 elem --> %lu", vit, ban);
*/

    return 0;
}
