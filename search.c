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
    char valid;
} nodeT;


char check_angle(nodeT a, nodeT b, nodeT c) {
    long ip_w = ((long)a.w - (long)b.w) * ((long)c.w - (long)b.w);
    long ip_x = ((long)a.x - (long)b.x) * ((long)c.x - (long)b.x);
    long ip_y = ((long)a.y - (long)b.y) * ((long)c.y - (long)b.y);
    long ip_z = ((long)a.z - (long)b.z) * ((long)c.z - (long)b.x);
    long sum = ip_w + ip_x + ip_y + ip_z;
    return (sum > 0);
}

char check_triplet(nodeT a, nodeT b, nodeT c) {
    return check_angle(a, b, c) && check_angle(b, c, a) && check_angle(c, a, b);
}

char check_new_point(nodeT new_point, nodeT* points, int count) {
    for (int i = 0; i < count; i++) {
        for (int j = i + 1; j < count; j++) {
            if (!check_triplet(new_point, points[i], points[j])) {
                return 0;
            }
        }
    }
    return 1;
}

nodeT find_point(nodeT* points, int count) {
    nodeT new_point;
    for (int i = 0; i < 10000; i++) {
        new_point.w = (unsigned short)rand();
        new_point.x = (unsigned short)rand();
        new_point.y = (unsigned short)rand();
        new_point.z = (unsigned short)rand();
        if (check_new_point(new_point, points, count)) {
            new_point.valid = 1;
            return new_point;
        }
    }
    new_point.valid = 0;
    return new_point;
}

int main(int argc, char** argv) {
    srand(time(0));
    int count = 9;
    nodeT* points = malloc(count * sizeof(nodeT));
    char found = 0;
    nodeT point;
    int i;
    do {
        for (i = 0; i < count; i++) {
            point = find_point(points, i);
            if (!point.valid) {
                break;
            }
            points[i] = point;
        }
    } while (i < count);

    for (int i = 0; i < count; i++) {
        printf("%d\t%d\t%d\t%d", points[i].w, points[i].x, points[i].y, points[i].z);
        printf("\n");
    }
    return 0;
}