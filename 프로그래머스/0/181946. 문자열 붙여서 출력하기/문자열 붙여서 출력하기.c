#include <stdio.h>
#define LEN_INPUT1 11
#define LEN_INPUT2 11

int main(void) {
    char str1[LEN_INPUT1];
    char str2[LEN_INPUT2];
    scanf("%s %s", &str1, &str2);
    printf("%s%s", str1, str2);

    return 0;
}