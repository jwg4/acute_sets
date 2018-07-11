#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct node{
    unsigned short w;
    unsigned short x;
    unsigned short y;
    unsigned short z;
    struct node* left;
    struct node* right;
    char depth;
} nodeT;


char check_triplet(nodeT a, nodeT b, nodeT c) {
    return 1;
}

char check_new_point(nodeT new_point, nodeT* points, int count) {
    return 1;
}

nodeT find_point(nodeT* points, int count) {
    nodeT new_point;
    do {
        new_point.w = (unsigned short)rand();
        new_point.x = (unsigned short)rand();
        new_point.y = (unsigned short)rand();
        new_point.z = (unsigned short)rand();
    } while (!check_new_point(new_point, points, count));
    return new_point;
}

int main(int argc, char** argv) {
    srand(time(0));
    int count = 10;
    nodeT* points = malloc(count * sizeof(nodeT));
    for (int i = 0; i < count; i++) {
        points[i] = find_point(points, i);
    }
    for (int i = 0; i < count; i++) {
        printf("%d\t%d\t%d\t%d", points[i].w, points[i].x, points[i].y, points[i].z);
        printf("\n");
    }
    return 0;
}
