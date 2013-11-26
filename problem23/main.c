#include <stdio.h>
#include <stdlib.h>

#include "func.h"

int main()
{
    /*printf(" --> %d", initPrime(28123));

    printf("isAbundant(23), %d", isAbundant(23));


    int *abarr = abArr(100);

    int i = 0;
    while(i < 100) {
        printf("%d\n", abarr[i]);
        i++;
    }





    //free(abarr); //comprends pas pourquoi sa fail
    */

    int len = 28123;

    int *a = abArr(len);

    int *tab = zgrublu(a,len);

    int res = sum(tab);

    printf("\n brii : %d\n", res);

    free(tab);

    /*
    int i = 0;
    while(i < len) {
        printf("%d\n", tab[i]);
        i++;
    }
*/
    return 0;
}
