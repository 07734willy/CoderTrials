#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

typedef struct {
	uint32_t cols;
	uint32_t rows;
	uint32_t x;
	uint32_t y;
	uint8_t dir; //N:00 E:01 S:10 W:11
	uint8_t* tiles;
	uint32_t errors;
} Board;

Board* makeBoard(uint32_t cols, uint32_t rows, char** self, char** other) {
	Board* board = malloc(sizeof(Board));
	board->tiles = malloc(cols * rows * sizeof(uint8_t));
	board->cols = cols;
	board->rows = rows;
	int i, j;
	for (i = 0; i < rows; i++) {
		for (j = 0; j < cols; j++) {
			board->tiles[j + i * cols] =  (self[i][j] == '#');
			board->tiles[j + i * cols] |= (self[i][j] != other[i][j]) << 1;
			board->errors += self[i][j] != other[i][j];
		}
	}
	return board;
}

Board* cloneBoard(Board* oldBoard) {
	Board* newBoard = malloc(sizeof(Board));
	memcpy(newBoard, oldBoard, sizeof(Board));
	
	newBoard->tiles = malloc(oldBoard->cols * oldBoard->rows * sizeof(uint8_t));
	memcpy(newBoard->tiles, oldBoard->tiles, oldBoard->cols * oldBoard->rows * sizeof(uint8_t));
	return newBoard;
}

int stepBoard(Board* board) {
	uint8_t* tile = board->tiles + board->x + board->y * board->cols;
	if (*tile & 1) {
		board->dir = (board->dir + 1) & 3;
	} else {
		board->dir = (board->dir - 1) & 3;
	}
	switch (board->dir) {
		case 0:
			board->y = (board->y - 1 + board->rows) % board->rows;
			break;
		case 1:
			board->x = (board->x + 1) % board->cols;
			break;
		case 2:
			board->y = (board->y + 1) % board->rows;
			break;
		case 3:
			board->x = (board->x - 1 + board->cols) % board->cols;
			break;
	}
	board->errors += 1 - (*tile & 2);
	*tile ^= 3;
	return board->errors == 0;
}
int stepBackBoard(Board* board) {
	switch (board->dir) {
		case 0:
			board->y = (board->y + 1) % board->rows;
			break;
		case 1:
			board->x = (board->x - 1 + board->cols) % board->cols;
			break;
		case 2:
			board->y = (board->y - 1 + board->rows) % board->rows;
			break;
		case 3:
			board->x = (board->x + 1) % board->cols;
			break;
	}
	uint8_t* tile = board->tiles + board->x + board->y * board->cols;
	*tile ^= 3;
	board->errors -= 1 - (*tile & 2);
	if (*tile & 1) {
		board->dir = (board->dir - 1) & 3;
	} else {
		board->dir = (board->dir + 1) & 3;
	}
	return board->errors == 0;
}

void printBoard(Board* board) {
	int i, j;
	for (i = 0; i < board->rows; i++) {
		for (j = 0; j < board->cols; j++) {
			if (board->tiles[j + board->cols * i] & 1) {
				printf("#");
			} else {
				printf(".");
			}
		}
		printf("\n");
	}
	printf("X: %u, Y: %u, Dir: %u, Err: %u\n", board->x, board->y, board->dir, board->errors);
}

int main(int argc, char** argv) {
	char c;
	scanf("%c", &c);
	uint8_t dir = 0;
	switch (c) {
		case 'W': dir++;
		case 'S': dir++;
		case 'E': dir++;
		default: break;
	}

	uint32_t x, y;
	scanf("%u %u", &x, &y);
	uint32_t cols, rows;
	scanf("%u %u", &rows, &cols);

	char** str1 = malloc(rows * sizeof(char*));
	char** str2 = malloc(rows * sizeof(char*));
	int i;
	for (i = 0; i < rows; i++) {
		str1[i] = calloc(cols + 1, sizeof(char));
		scanf("%s", str1[i]);
	}
	for (i = 0; i < rows; i++) {
		str2[i] = calloc(cols + 1, sizeof(char));
		scanf("%s", str2[i]);
	}
	Board* board1 = makeBoard(cols, rows, str1, str2);
	board1->x = x;
	board1->y = y;
	board1->dir = dir;
	Board* board2 = cloneBoard(board1);

	uint64_t count = 0;
	if (board1->errors == 0) {
		printf("%lu\n", count);
		return 0;
	}
	while (1) {
		count++;
		if (stepBoard(board1) || stepBackBoard(board2)) {
			printf("%lu\n", count);
			return 0;
		}
		if ((count & 0xFFFFFF) == 0) {
			printf("%lu\n", count);
		}
		//553648128
		if (count == 934920047) {
			printBoard(board1);
			printBoard(board2);
			return 0;
		}
	}
}
