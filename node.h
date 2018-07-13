#ifndef NODE_H
#define NODE_H

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

#endif
