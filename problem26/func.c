#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <gmp.h>

#include "func.h"



int countSubstring(const char *num, const char *pat) {

    char *str = num, *sub = pat;

    int length = strlen(sub);
    int occur = 0;

    //printf("\n\t\t\t str -> %.*s sub -> %s", 200, str, sub);

    if (length == 0) return 0;

    for (str = strstr(str, sub); str; str = strstr(str + length, sub))
        ++occur;
    return occur;
}


int recurringCyle(mpf_t m) {

    int count_p = 0, i, len;

    char *pattern, *num;

    mp_exp_t exponent;

    //trnsformation du nombre en char *
    num = mpf_get_str(NULL, &exponent, 10, 0, m);
    len = strlen(num);
    num[len] = '\0';

    //printf(" num -> %s ; length -> %d \n", num, len);

    //Allocation du tableau pattern
    pattern = malloc(len/2);

    // On boucle sur la moitié du nombre
    for (i = 0; i < len/2; i++) {

        //on incremente le pattern, ie on augmente la taille du pattern
        pattern[i] = num[i];

        //probleme d'initialisation de tableau avec des valeurs random :'(
        pattern[i+1] = '\0';

        //On compte le nombre de substring qui match 'pattern' dans les decimales
        int c = countSubstring(num, pattern);

        //Debugger aux printf c'est assez sale
        //printf("\n\t  i-> %d ; pattern -> %s; countSub -> %d ; to Reach -> %d", i, pattern, c, (int)(len/(i+1)));

        //si on a un nb de pattern == (nbDecimales)/(tailleduPattern)
        if ( c == (int)(len/(i+1)) ){
            printf("\t\ti : %d ;\n", i);
            count_p = i+1;
            break;
        }
    }

    //printf("\ti = %d, pattern -> %.*s ; count -> %d", i, count_p, pattern, count_p);

    free(pattern);
    free(num);
    return count_p;
}

/*int max (int a, int b) {
    return (a>b)?a:b;
}*/
