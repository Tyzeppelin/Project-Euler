#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <gmp.h>
#include <math.h>

#include "func.h"

int main() {

    int max = 0, i_max = 0;
    double i;
    mpf_t m, n, r;

    mpf_set_default_prec(4*PRECISION);

    mpf_init_set_d(m, 1.0);

    for (i = 1.0; i < 1000; i++) {
        mpf_init_set_d(n, i);
        mpf_init(r);
        mpf_div(r, m, n);
        printf("\n\ni -> %.0lf", i);
        int c = recurringCyle(r);
        if(max < c){
            max = c;
            //c_max = c;
            i_max = i;
        }
    }


    printf("\n\n----------\nMAXIMUM POWAAAA\ni : %d,  %d numbers\n----------", i_max, max);

    return 0;
}
