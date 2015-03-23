#include <stdio.h>
#include <stdlib.h>


int record(){
    system("rec -c 2 miaudio.wav trim 0 5");
    return 0;
}
int main()
{
    record();
    return 0;
}