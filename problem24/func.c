
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

/**
 * toReach  --> number to reach
 * n        --> while fact(n)*i < toReach
*/
int interleave(int toReach, int n) {

    int i = 1, m = 0;

    if(toReach <= n) {return 0;}

    while (m < toReach && i < n) {
        i++;
        m = i*fact(n);
        //printf("\n\ttoReach : %d, m : %d, i : %u", toReach, m, i);
    }
    if (m == 0) {return i;}
    //printf("\n\t final toReach : %d, m : %d, i : %u", toReach, m, i);
    return i-1;
}

/**
 * find the nth elements of a nElem permutation
 */
long unsigned int position(int nth, int nElem) {

    int i;
    long int res = 0;
    int reach = nth;

    for (i = nElem-1; i > 0; i--) {
        int k = interleave(reach, i);
        res = res*10 + k;
        reach = reach - k*fact(i);
        printf("\nreach -> %d; i -> %d; res -> %lu", reach, i, res);
    }

    return res*10;
}

long unsigned int traduction(int *arr, int len, long int seq) {
    long int res = 0;
    int i = 0;
    long unsigned int s =  seq;

    for (i = len; i > 0; i--) {
        long int k = pop(arr, i, s/pow(10, i-1));
        if (k != 0) {s -= (long unsigned int)(s/pow(10 ,i-1))*pow(10, i-1);}

        res = res*10+k;

        printf("\ni : %d, k : %lu, res : %lu seq restante : %lu  ; ", i, k, res, s);
        printArr(arr, i);
    }


    return res;
}

/*
 * Care : i is the position in arr
*/
int pop (int *arr, int len, int i) {

    int j, k = 0, res = arr[i];
    for (j = 0; j < len-1; j++) {
        if (j == i) {k++;}
        arr[j] = arr[k];
        k++;
    }

    return res;
}




int *sale (int toReach) {

int n = 10;
int a, b, c, d, e, f, g, h, i;
int countToReach = 0;
int *res  = (int *)malloc(10*sizeof(int));

for (a = 0; a < n; a++) {
        res[0] = a;
    for (b = 0; b < n; b++) {
        if (b != a) {
            res[1] = b;
            for (c = 0; c < n; c++) {
                if (c != a && c!= b) {
                    res[2] = c;
                    for (d = 0; d < n; d++) {
                        if (d != a && d != b && d != c) {
                            res[3] = d;
                            for (e = 0; e < n; e++) {
                                if (e != a && e !=b  && e != c && e!= d) {
                                    res[4] = e;
                                    for (f = 0; f < n; f++) {
                                        if (f != a && f != b && f != c && f != d && f != e) {
                                            res[5] = f;
                                            for (g = 0; g < n; g++) {
                                                if (g != a && g != b && g != c && g != d && g != e && g != f) {
                                                    res[6] = g;
                                                    for (h = 0; h < n; h++) {
                                                        if (h != a && h != b && h != c && h != d && h != e && h != f && h != g) {
                                                            res[7] =  h;
                                                            for (i = 0; i < n; i++) {
                                                                if (i != a && i != b && i != c && i != d && i != e && i != f && i != g && i != h) {
                                                                    res[8] = i;
                                                                    //printf("\ncount : %lu, res -> %lu", countToReach, res);
                                                                    countToReach++;
                                                                }
                                                                if (countToReach == toReach) {
                                                                    return res;
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }

        }
    }
}
//printArr(res, 10);
return res;

}

void printArr(int* arr, int len){
    int i;
    printf("\n");
    for (i = 0; i < len; i++) {
        printf("%d, ", arr[i]);
    }
    printf("\n");
}
