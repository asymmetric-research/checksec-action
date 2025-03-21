#include <stdio.h>
#include <string.h>

int main() {
    char buf[10];
    char *input = "This is a long string that will overflow the buffer";
    strcpy(buf, input);  // Potentially unsafe
    printf("Buffer: %s\n", buf);
    return 0;
}