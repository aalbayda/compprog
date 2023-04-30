// Greedy graph coloring algorithm
// Exercise from CMSC142 (Analysis of Algorithms)

#include <malloc.h>
#include <stdio.h>

// Linked list node structure
typedef struct node {
    int x;
    struct node *next;
    struct node *tail;
} graph;

// Create a new node
graph *Node(int x) {
    struct node *newNode = malloc(sizeof(struct node));
    newNode->x = x;
    newNode->next = NULL;
    newNode->tail = newNode;
    return newNode;
};

int *graphColoring(graph **, int);
int getAvailableColor(graph **, int *, int, int);
void viewColor(int *, int);
void deleteGraph(graph **, int);

int main() {
    graph **g;
    int v, e;
    int *color;

    // Take input
    scanf("%d", &v);
    scanf("%d", &e);

    // Instantiate memory for graph (an adjlists for each vertex)
    // O(V)
    g = malloc(v * sizeof(struct node *));
    for (int i = 0; i < v; i++) {
        g[i] = Node(i);
    }

    // Store each edge via the adj list
    // O(E)
    int src, dest;
    printf("Adjacency List\n");
    for (int i = 0; i < e; i++) {
        scanf("%d %d", &src, &dest);
        struct node *temp = NULL;

        // Undirected so add the vertex both ways
        // O(1)
        g[src]->tail->next = Node(dest);
        g[src]->tail = g[src]->tail->next;
        g[dest]->tail->next = Node(src);
        g[dest]->tail = g[dest]->tail->next;
    }

    // Print
    for (int i = 0; i < v; i++) {
        printf("%d->", g[i]->x);
        struct node *temp = NULL;
        temp = g[i]->next;
        while (temp) {
            printf("%d", temp->x);
            if (temp->next) printf("->");
            temp = temp->next;
        }
        printf("\n");
    }
    printf("\n");

    // Determine colors
    color = graphColoring(g, v);
    viewColor(color, v);

    // Garbage collection
    free(color);
    deleteGraph(g, v);
}

int *graphColoring(graph **g, int v) {
    int *color, availCol, i;

    // Colors are represented as integers starting from 0
    color = (int *)malloc(sizeof(int) * v);
    // -1 means vertex is not yet assigned a color
    for (i = 0; i < v; i++) color[i] = -1;

    color[0] = 0;  // Assign first vertex with the first color
    for (i = 1; i < v; i++) {
        // Next vertex assigned an available color
        availCol = getAvailableColor(g, color, v, i);
        color[i] = availCol;
    }
    return color;
}

int getAvailableColor(graph **g, int *color, int v, int curr) {
    graph *p;
    int *available, i, availCol;

    // Color tracker - if 1, available, if 0 it's allocated to a neighboring
    // vertex
    available = (int *)malloc(sizeof(int) * (v));
    for (i = 0; i < v; i++) available[i] = 1;  // boolean

    // Algo goes like this
    // 1. check all adjacent vertices
    // 2. check the color of the adjacent vertices
    // 3. if color is not -1: available[color[i]] = 0
    struct node *temp = NULL;
    temp = g[curr];
    while (temp->next) {
        temp = temp->next;
        if (color[temp->x] > -1) {
            available[color[temp->x]] = 0;
        }
    }

    for (i = 0; i < v; i++) {  // get the smallest color that is available
        if (available[i] == 1) {
            availCol = i;
            break;
        }
    }

    free(available);
    return availCol;
}

void viewColor(int *color, int v) {
    int i;
    for (i = 0; i < v; i++) {
        printf("Vertex %d -> Color %d\n", i, color[i]);
    }
}

void deleteGraph(graph **g, int v) {
    int i;
    graph *p;
    for (i = 0; i < v; i++) {
        while (g[i] != NULL) {
            p = g[i];
            g[i] = g[i]->next;
            free(p);
        }
    }
    free(g);
}