// Subset sum problem - exercise from Analysis of Algorithms class

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Comparison function used for qsort()
int comp(const void *a, const void *b) {
    int *x, *y;
    x = (int *)a;
    y = (int *)b;
    return (*x - *y);
}

int main() {
    // Get input S
    int n;
    printf("Number of elements in S: ");
    scanf("%d", &n);
    int s[n];
    printf("Enter the sequence S: ");
    for (int i = 0; i < n; i++) scanf("%d", &s[i]);

    // Sort the array S
    qsort(s, n, sizeof(int), comp);

    // Get input k
    int k;
    printf("k: ");
    scanf("%d", &k);

    // Create DP table
    int dp[n][k + 1];
    memset(dp, 0, sizeof(dp));

    // Fill in first column with 1's
    for (int i = 0; i < n; i++) dp[i][0] = 1;

    // Store sums for each row
    for (int i = 0; i < n; i++) {
        for (int j = 1; j < (k + 1); j++) {
            // Initial row is just flipping the jth element to 1
            if (i == 0) {
                if (j == s[i]) {
                    dp[i][j] = 1;
                    continue;
                }
            }
            // Succeeding rows use the shortcut "|" method
            else {
                if (j < s[i])
                    dp[i][j] = dp[i - 1][j];
                else
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - s[i]];
            }
        }
    }

    // print DP
    printf("\nDP Table\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < (k + 1); j++) {
            printf("%d ", dp[i][j]);
        }
        printf("\n");
    }

    // If last cell is 0, there is no solution
    if (!dp[n - 1][k]) {
        printf("\nNo solution.\n");
        return 1;
    }

    // Find solution set
    int solution[n];
    int solution_i;

    // Find "highest 1"
    int i = 0;
    for (; i < n; i++) {
        if (dp[i][k] == 1) break;
    }

    // Backtrack from there
    while (i > -1) {
        // If we reach the 1st column dont include to soltn set
        if (k == 0) break;
        // Store to soln set
        solution[solution_i++] = s[i];
        k -= s[i];
        i -= 1;
    }

    // Print solution set
    printf("\nSolution Set\n{ ");
    for (int i = solution_i - 1; i > -1; i--) printf("%d ", solution[i]);
    printf("}\n");
}