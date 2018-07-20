#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "node.h"
#include "check.h"

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
    if(argc>=2) {
        count = atoi(argv[1]);
        printf("Using %d as the number of points to search for\n", count);
    }

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
