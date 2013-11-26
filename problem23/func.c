
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "func.h"


int isAbundant(int n) {


    int sum = 1;
    int i;

    for (i = 2; i <= n/2; i++) {
        if (n % i == 0) {
            sum += i;
        }
    }
    return sum > n;
}

int *abArr (int n) {

    int num = 0;
    int i, j;



    int *ab = (int*)malloc((n+1)*sizeof(int));
    if (ab == NULL) {
            fprintf(stdout, "pwoblem ab");
            exit(0);
    }



    for (j = 0; j < n; j++) {
        ab[j] = -1;
    }

    for (i = 1; i < n; i++) {
        if (isAbundant(i)){
                ab[num++] = i;
        }
    }

    return ab;
}

int *zgrublu(int* ab, int n) {

    int i, j;
    int countAd = 0;


    int *entier = (int*)malloc(n*sizeof(int));
    if (entier == NULL) {
            fprintf(stdout, "pwoblem entier");
            exit(0);
    }



    for (i = 0; i < n; i++) {
        entier[i] = i;
    }


    for (j = 0; j < n; j++) {
            if (ab[j] != -1) {
                countAd++;
            }
    }


    for (i = 0; i < countAd; i++) {
        for (j = 0; j < countAd; j++) {
            if (ab[i]+ab[j] < n && ab[i]+ab[j] > 0) {
                 entier[ab[i]+ab[j]] = -1;
            }
        }
    }



    int *res = (int*)malloc((countAd+1)*sizeof(int));
    if (res == NULL) {exit(0);}

    i = 0;
    for (j = 0; j < n; j++) {
        if (entier[j] != -1 && i < countAd) {
            //printf("%d\t", entier[j]);
            res[i] = entier[j];
            i++;
            }
    }
    res[countAd] = 0;

    return res;
}


int sum(int *ab) {

    int i = 0, sumN = 0;

    while(ab[++i] != 0) {
        sumN += ab[i];
    }
    return sumN;
}
