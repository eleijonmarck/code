#include <stdint.h>
#include <stdio.h>

int main(){

	int a = sizeof(int8_t);
	int b = sizeof(int16_t);
	int c = sizeof(int32_t);
	int d = sizeof(int64_t);

	int aa = sizeof(short);
	int bb = sizeof(int);
	int cc = sizeof(long);
	int dd = sizeof(long long);

	printf("%d,%d,%d,%d\n", a,b,c,d);
	printf("%d,%d,%d,%d\n",aa,bb,cc,dd);
}

