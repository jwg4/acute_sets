#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int check_angle(int a, int b, int c)
{
    return (
        ( (a ^ b) & (b ^ c) )
        && ( (b ^ a) & (a ^ c) )
        && ( (a ^ c) & (c ^ b) )
    );
}

int check_set(int new_value, int* values, int count){
    for (int i = 0; i < count; i++) {
        for (int j = i + 1; j < count; j++) {
            if (!check_angle(new_value, values[i], values[j])){
                return 0;
            }
        }
    }
    return 1;
}

int find_acute_set(int dimension, int size){
    int mask = (1 << dimension) - 1;
    int count = 0;
    int* array = malloc(size * sizeof(int));

    if (mask > RAND_MAX) {
        printf("Failed, because the dimensions was too big to generate random numbers");
        return -1;
    }

    while (count < size) {
        int found = 0;
        int value;
        for (int i = 0; i < 1000; i++){
            value = rand() & mask;
            if (check_set(value, array, count)) {
                found = 1;
                break;
            }
        }
        if (found) {
            array[count] = value;
            count++;
        } else {
            count--;
        }
    }
    
    for (int i = 0; i < count; i++){
        printf("%x\t", array[i]);
    }
    printf("\n");
}
        
int main(int argc, char** argv){
    int dimension = 4;
    int size = 5;

    srand((unsigned) time(NULL));

    find_acute_set(dimension, size);    
}
