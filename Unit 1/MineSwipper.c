#include<stdio.h>
void main()

{
    int n,m,i,j,k,w,z;
    int x,y;
    char a[100][100];
    int b[100][100];

    scanf("%d %d",&n,&m);
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            scanf(" %c",&a[i][j]);
            if(a[i][j]=='*')
                b[i][j]='42';
            else
                b[i][j]=0;
        }
    }
    //main logic
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
        if(a[i][j]=='*')
            {
                x=i;w=j;
                for(y=x-1;y<=x+1;y++)
                {
                    for(z=w-1;z<=w+1;z++)
                    {
                        k=b[y][z];
                        b[y][z]=k+1;
                    }
                }
            }
        }
    }


    //displaying
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
           if(a[i][j]=='*')
               printf("%c ",a[i][j]);
           else
            printf("%d ",b[i][j]);
        }printf("\n");
    }


}//end of main
