// Albayda and Resoles, CMSC 142 Exercise 9

#include <stdio.h>
#include <stdlib.h>

int main() {
    int N;
    printf("Enter N: ");
    scanf("%d", &N);

    int start, move;
    int *nopts = (int *)malloc((N + 2) * sizeof(int));
    int **option = (int **)malloc((N + 2) * sizeof(int *));
    for (int i = 0; i < N + 2; i++)
        option[i] = (int *)malloc((N + 2) * sizeof(int));

    int i, candidate;

    move = start = 0;
    nopts[start] = 1;

    // traverse while dummy stack isnt empty
    while (nopts[start] > 0) {
        // move forward
        if (nopts[move] > 0) {
            move++;
            nopts[move] = 0;

            // everything > previous move is a candidate
            for (candidate = option[move - 1][nopts[move - 1]] + 1;
                 candidate <= N; candidate++) {
                option[move][++nopts[move]] = candidate;

                // print move (space instead of %2i to support >2-digit numbers)
                for (i = 1; i <= move; i++) printf(" %i ", option[i][nopts[i]]);
                printf("\n");
            }
        } else {  // backtrack
            move--;
            nopts[move]--;
        }
    }

    for (int i = 0; i < N + 2; i++) free(option[i]);
    free(option);
    free(nopts);
}