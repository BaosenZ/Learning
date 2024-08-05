#include <stdio.h>

int main()
{
    int value = 28;    // Variable declaration
    int *ptr = &value; // Pointer declaration

    printf("value: %d\n", value);
    printf("&value return memory address: %p\n", &value);
    printf("ptr return memory address (reference): %p\n", ptr);
    printf("*ptr return the value (dereference): %d\n", *ptr);
}