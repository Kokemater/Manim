#include <stdio.h>
#define N 4

void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
void print_list(int *list, int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%d < ", list[i]);
    }
    printf("\n");
}
int main(void)
{
    int list[N] = {1, 3, 2, 0};
    int i;
    int j;

    i = 0;
    while (i < N)
    {
        j = 0;
        while(j < N - 1)
        {
            if (list[j] > list[j+1])
                swap(&list[j], &list[j+1]);
            j++;
        }
        i++;
    }

    print_list(list, N);

}