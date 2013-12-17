#ifndef FUNC_H_INCLUDED
#define FUNC_H_INCLUDED

#include <stdio.h>

int fact (int n);

int interleave(int n, int nb);

long unsigned int position(int nToReach, int nElem);

long unsigned int traduction(int* arr, int len, long int seq);

int pop (int *arr, int len, int i);

void printArr(int* arr, int len);

int *sale (int toReach);


#endif // FUNC_H_INCLUDED
