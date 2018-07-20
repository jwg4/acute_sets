#include <stdio.h>

#include "node.h"

char check_angle(nodeT a, nodeT b, nodeT c) {
    long ip_w = ((long)a.w - (long)b.w) * ((long)c.w - (long)b.w);
    long ip_x = ((long)a.x - (long)b.x) * ((long)c.x - (long)b.x);
    long ip_y = ((long)a.y - (long)b.y) * ((long)c.y - (long)b.y);
    long ip_z = ((long)a.z - (long)b.z) * ((long)c.z - (long)b.z);
    long sum = ip_w + ip_x + ip_y + ip_z;
    return (sum > 0) ? 1 : 0;
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
