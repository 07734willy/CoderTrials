#include <stdio.h>

int main() {
	struct {
		unsigned int mantissa: 23;
		unsigned int exp: 8;
		unsigned int sign: 1;
	} bits;
	scanf("%f", (float*)&bits);
	printf("%u\n", bits.exp);
}
