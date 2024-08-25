#include <stdio.h>
#define N 5

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
    int list[N] = {2, 3, 8, 5, 6};
    int i;
    int j;
    int min_index;

    i = 0;
    while (i < N - 1)
    {
        j = i;
        min_index = i;
        while(j < N)
        {
            if (list[j] < list[min_index])
                min_index = j;
            j++;
        }
        if (min_index != i)
        {
            swap(&list[i], &list[min_index]);
        }
        i++;
    }

    print_list(list, N);

}