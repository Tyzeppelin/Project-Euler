
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

int interleave(int N, int nbElem) {

    int i = 0, j = 0;

    while (i - N < 0) {
        i = (++j)*fact(nbElem);
        // printf("\n\ti : %d, N : %d, j : %d", i, N, j);
    }

    return j;
}

int position(int nToReach, int nElem) {

    int i = 0;
    int rest = 0;
    int att = nToReach;
    int result = 0;


    for(i = nElem-1; i >= 1; i--) {

        int a = interleave(att, i);
        result = result*10+a;
        rest = a * fact(i)-att;
        att = fact(i)-rest;
        // printf("\na --> %d, result--> %d, rest --> %d, att --> %d.\n", a, result, rest, att);
    }

    return 10*result+1;
}

int traduction(int *arr, int len, int seq) {

    int i = 0, res = 0, pl = 0;
    int mod = len-1;

    for (i = 0; i < len-1; i++){
        pl = (int)seq/pow(10, mod);

        int k = pop(arr, len, pl);
        res = res*10 + k;

        seq = seq % (int)pow(10, mod);
        mod--;
        //printf("\npl --> %d, mod --> %d, k--> %d, res --> %d, seq --> %d.", pl, mod, k, res, seq);
    }

    return 10*res + arr[0];
}

/*
 * Care : i is the nth int,not mean the position in arr
*/
int pop (int *arr, int len, int i) {

    int j, k = 0, res = arr[i-1];
    for (j = 0; j < len-1; j++) {
        if (j == i-1) {k++;}
        arr[j] = arr[k];
        k++;
    }

    return res;
}
