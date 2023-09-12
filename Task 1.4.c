#include <stdio.h>
#include <stdlib.h>
float kalman(float mpu_v,float bno_v,float mpu_a,float bno_a)
{
    float kgc=mpu_a/(mpu_a+bno_a);
    float r=bno_v+kgc*(mpu_v-bno_v);
    return r;
}
int main()
{
    float mpu[10]={0.0,11.68,18.95,23.56,25.72,25.38,22.65,18.01,10.14,-0.26};
    float bno[10]={0.0,9.49,16.36,21.20,23.16,22.8,19.5,14.85,6.79,-2.69};
    float measure[10];
    int size=sizeof(mpu)/sizeof(mpu[0]);
    printf(" AVERAGE MEASURE: ");
    for(int i=0;i<size;i++)
        measure[i]=kalman(mpu[i],bno[i],78,92);
    for(int i=0;i<size;i++)
        printf("%.3f  ",measure[i]);

    return 0;
}
