#include <stdio.h>
#define LEN_INPUT 11
#define _CRT_SECURE_NO_WARNINGS

int main(void) {
    char str[LEN_INPUT];
    int n;
    scanf("%s %d", &str, &n);
    for(int i = 0; i < n; i++)
    {
        printf("%s", str);
    }
    return 0;
}