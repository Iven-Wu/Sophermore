#include <iostream>
#include <vector>
#include <algorithm>
#include<stdio.h>
using namespace std;

int num = 0;
int assign[81];
int a[9][9];
void print(int a[9][9]){
	FILE *fp;
	fp = fopen("outsudoku.txt","w+");
    for(int i=0;i<9;i++){
       for(int j=0;j<9;j++){
           fprintf(fp,"%d ",a[i][j]);
           cout<<a[i][j]<<" ";

       }
       cout<<endl;
	   fprintf(fp,"\n");
   }
   cout<<endl;
   fprintf(fp,"\n");
}
bool finish(int a[9][9])
{
	for(int i=0;i<9;i++){
		for(int j=0;j<9;j++){
			if (a[i][j]==0)
				return false;
		}
	}
	return true;
}
bool judge(int x,int y,int a[9][9]){


   for(int i=0;i<9;i++){  					//ÐÐ
       if(a[x][i]==a[x][y]&&i!=y)
	   return false;
        if(a[i][y]==a[x][y]&&i!=x)
       return false;
   }
   for(int i=x/3*3;i<x/3*3+3;i++){  		//·½¸ñ
       for(int j=y/3*3;j<y/3*3+3;j++){
           if(a[i][j]==a[x][y]&&(i!=x||j!=y))
	   		return false;

       }
   }
   /*if(x==y){
   		for(int i=0;i<9;i++){
   			if(a[i][i]==a[x][y] &&(i!=x))
				return false;
		}
   }
   if (x+y==8){
		for(int i=0;i<9;i++){
			if(a[i][8-i]==a[x][y] && (i!=x))
				return false;
		}
   }*/
   return true;
}
void BT(int level,int a[9][9])
{
	//cout<<level;
	int k=0;
	num++;
	int v = 0;
	if(finish(a) == true)
	{
		print(a);
		return;
	}
	int i;
	int j;
	for(i=0;i<9;i++){
		for(j=0;j<9;j++){
			if(a[i][j]==0){
				k=1;
				break;
			}
		}
		if(k==1) break;
	}
	for(k = 1; k <= 9; k++)
	{
		a[i][j] = k;
		if(judge(i, j,a) == true){
			BT(level + 1,a);
		}
		else continue;
	}
	a[i][j] = 0;
	return;
}
int main()
{
	int i,j;
	FILE *fp;
	//int a[9][9];
	if((fp=fopen("sudoku.txt","rt"))==NULL)
	{
		printf("cannot open");
		return 0 ;
	}
	for(i=0;i<9;i++){
		for(j=0;j<9;j++){
			fscanf(fp,"%d\n",&a[i][j]);
		}
	}

	fclose(fp);
	for(i=0;i<9;i++){
		for(j=0;j<9;j++){
			printf("%d ",a[i][j]);
		}
		printf("\n");
	}
	printf("\n\n\n");
	BT(0,a);
}





