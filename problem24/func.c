
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

int interleave(int N, int nbElem) {

    int i = 0, j = 0;

    while (i - N <= 0) {
        i = (++j)*fact(nbElem);
        //printf("\ni : %d, N : %d, j : %d", i, N, j);
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
        printf("\nres : %d", result);
    }

    return result;
}

int traduction(int *arr, int len, int seq) {

    int i = 0, res = 0, pl = 0;

    for (i = 0; i < len; i++){
        pl = (int)seq/pow(10, len-i)
        res += res*10 + pop(arr, len, pl);
    }

    return res;
}
int pop (int *arr, int len, int i) {

    return 0;
}
