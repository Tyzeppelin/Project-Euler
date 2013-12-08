#include <stdio.h>
#include <stdlib.h>

#include "func.h"

int main()
{


    int len = 10;
    int reach = 1000000;
    int nb[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};


    printf("Resolution pour [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n");
    printf("\n On cherche le 1000000!\n\n");

    int vit = position(reach, len-1);

    printf("\n Position dans le tableau d'int --> %d", vit);

    int ban = traduction(nb, 10, vit);

    printf("\ntrad de %d dans un e arr de 10 elem --> %d", vit, ban);


    return 0;
}
