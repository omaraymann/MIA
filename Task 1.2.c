#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int x;
    do{
        printf("ENTER AN INPUT: ");
        scanf("%d",&x);
    }while(x<0);
    for(int i=x;i>0;i--)
    {
        printf("%d\n",i);
        sleep(1);
    }
    printf("BLAST OFF TO THE MOON!");

    return 0;
}
