#include <stdio.h>

#include "check.h"

int main(int argc, char** argv) {
    nodeT a, b, c;
    a.w = 56770;
    a.x = 48223;
    a.y = 32495;
    a.z = 61005;
    b.w = 30786;
    b.x = 16038;
    b.y = 32897;
    b.z = 29414;
    c.w = 16559;
    c.x = 10717;
    c.y = 26951;
    c.z = 33219;
    char result = check_triplet(a, b, c);
    printf("Result: %d", result);
    return 0;
}
