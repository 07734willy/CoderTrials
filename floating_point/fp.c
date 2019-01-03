#include <stdio.h>
#include <stdint.h>

int main() {
	uint32_t bits;
	scanf("%f", (float*)&bits);
	printf("%u\n", (bits >> 23) & 0xFF);
}
