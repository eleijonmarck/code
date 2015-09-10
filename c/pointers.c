#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    int i = 5, j = 6, k = 7;
    int *ip1 = &i, *ip2 = &j;
    int** ipp = &ip1;
    printf("address of value i: %p\n", &i);
    printf("address of value j: %p\n", &j);
    printf("value ip1: %p\n", ip1);
    printf("value ip2: %p\n", ip2);
    printf("value ipp: %p\n", ipp);
    printf("address value of ipp: %p\n", *ipp);
    printf("value of address value of ipp: %d\n", **ipp);
    *ipp = ip2;
    printf("value ipp: %p\n", ipp);
    printf("address value of ipp: %p\n", *ipp);
    printf("value of address value of ipp: %d\n", **ipp);
}

/*
Simply
& --> Address of
* --> Value at
*/
