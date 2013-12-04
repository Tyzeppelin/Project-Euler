
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "func.h"


 int fact (int n) {
    int i = 0, sum = 1;
    while (i < n)
        sum *= ++i;
    return sum;
}

//Marche pas

int interleave(int n, int nbElem) {

    int f = fact(nbElem-1);
    int res = 0;

    while (res*f < n) {
        ++res;
    }
    for (res = 0; res*f < n; res++);
    return res-1;
}

int* position(int* elem, int nToReach, int nElem) {

    int i = 0;
    int n = nToReach;

    int *res = (int*)malloc(nElem*sizeof(int));
    if (res == NULL) exit(0);

    for (i = 1; i < nElem; i++) {

        printf("\nnAAtteindre : %d, rank : %d, res[i-1] : %d", n, nElem-1, res[i-1]);

        res[i] = elem[interleave(n, nElem)];
        printf("\n trouvé : %d*%d!", res[i], nElem);
        n = n - res[i]*fact(nElem-1);
        nElem--;
    }

    return res;
}

int traduction(int* arr, int len) {

    int i = 0, res = 0;

    for (i = 0; i < len; i++){
        res += (arr[i]*(pow(10, len-i-1)));
    }

    return res;
}
