#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

uint16_t hash1(uint32_t n) {
	return n % 65521;
}

uint16_t hash2(unsigned long long n) {
	return ((n * 11400714819323198485LLU) >> 48) & 0xFFFF;
}

int main() {
	uint8_t* container = calloc((1L << 32), sizeof(uint8_t));
	uint16_t h1 = 0;
	uint16_t h2 = 0;
	uint64_t i;
	for (i = 0; i < (1L << 32); i++) {
		h2 = hash2(i);
		if (h2 == h1) {
			//printf("%lu, ", i);
			container[h1] += 1;
		}
		h1 += 1;
		if (h1 == 65521) {
			h1 = 0;
		}
	}
	for (i = 0; i < (1L << 32); i++) {
		if (container[i] > 1) {
			printf("%lu, ", i);
		}
	}
}
