
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "func.h"

int initPrime(int n) {

    int num =1;
    int i = 1;
    int* prime = (int*)malloc(n);

    if (prime == NULL) return -1;

    prime[0] = 2;

    for (i = 3; i < n; i++) {
        int j;
        int b = 1;
        for (j = 0; j < num; j++) {
            if (i % prime[j] == 0) {
                b = 0;
                break;
            }
        }
        if(b) {
            prime[num++] = i;
        }
    }

    realloc(prime, num);
    printf("%d,%d,%d,%d", prime[0], prime[1], prime[3], prime[num-1]);

    FILE* mem = NULL;

    mem = fopen("prime.array", "wb");

    for(i=0; i<num; i++)
        fprintf(mem, "%d ", prime[i]);

    free(prime);

    return num;
}

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
                //sprintf("%d. %d\n", num, i);
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
            printf("%d\t", entier[j]);
            res[i] = entier[j];
            i++;
            }
    }
    printf("\n old : %d", res[countAd]);
    res[countAd] = 0;
    printf(" new : %d\n", res[countAd]);

    return res;
}


int sum(int *ab) {

    int i = 0, sumN = 0;

    while(ab[++i] != 0) {
        sumN += ab[i];
    }
    return sumN;
}
