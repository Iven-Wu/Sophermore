#include <iostream>  
#include <vector>  
#include <algorithm> 
#define N 9 
using namespace std;  
int num = 0;
int assign[81];
int choice[N][N][N+1];           // 其中 [][][0] 代表可填数字的数量 对应的1到9 代表是否可以填该数字

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

bool finish(int a[N][N])
{
	for(int i=0;i<N;i++){
		for(int j=0;j<N;j++){
			if(a[i][j]==0)
				return false;
		}
	}
	return true;	
}
bool judge(int x,int y,int a[N][N]){  
	int s = x/3*3;
	int t =y/3*3;
   for(int i=0;i<N;i++){  
       if(a[x][i]==a[x][y]&&i!=y)  
            return false; 
		if(a[i][y]==a[x][y]&&i!=x)  
            return false; 
		if(a[s+i/3][t+i%3]==a[x][y]&&(s+i/3)!=x)
			return false;
   }  
   /*for(int i=0;i<9;i++){  
        
   }  
   for(int i=x/3*3;i<x/3*3+3;i++){  
       for(int j=y/3*3;j<y/3*3+3;j++){  
           if(a[i][j]==a[x][y]&&(i!=x||j!=y))  
                return false;  
       }  
   } */
   if(x==y){
   		for(int i=0;i<N;i++){
   			if(a[i][i]==a[x][y] &&(i!=x))
				return false;	
		}
   }
   if (x+y==8){
		for(int i=0;i<N;i++){
			if(a[i][N-1-i]==a[x][y] && (i!=x))
				return false;
		}
   }
   return true;  
}  
void minus1(int i, int j,int num){
	int ii=i/3*3;
	int jj=j/3*3;
    for(int k=0;k<N;k++){
        choice[i][k][num]--; 
        choice[k][j][num]--;
        choice[i][k][0]--; 
        choice[k][j][0]--;
        choice[ii+k/3][jj+k%3][num]--;
		choice[ii+k/3][jj+k%3][0]--;
    }
}

void plus1(int i, int j,int num){
	int ii=i/3*3;
	int jj=j/3*3;
    for(int k=0;k<N;k++){
        choice[i][k][num]++; 
        choice[k][j][num]++;
        choice[i][k][0]++; 
        choice[k][j][0]++;
        choice[ii+k/3][jj+k%3][num]++;
		choice[ii+k/3][jj+k%3][0]++;
    }
}

void BT(int level,int a[N][N])
{
	num++;
	int v = 0;
	int minp = 100;
	if(finish(a)==true){
		print(a);
		return;
	}
	int x,y;
	int flag = 0;
	for(int i=0;i<N;i++){
		for(int j=0;j<N;j++){
			if(a[i][j]==0){
				if(choice[i][j][0]<minp){
					minp = choice[i][j][0];
					x = i;
					y = j;
				}
			}
		}
	}

	for(int i = 1; i <= N; i++)
	{
        if(choice[x][y][i]==0)
           continue;
		a[x][y] = i;			    //去试每一个数字
        minus1(x,y,i);
		bool constraintsOK = true;
		if(judge(x, y,a) == true)
		{
            BT(level + 1,a);
		}
		plus1(x,y,i);
	}
	a[x][y] = 0;
	return;
}

int main()
{
	int i,j;
	FILE *fp;
	int a[N][N];
	if((fp=fopen("sudoku03.txt","rt"))==NULL)
	{
		printf("cannot open");
		return 0 ; 
	}
	for(i=0;i<N;i++){
		for(j=0;j<N;j++){
			fscanf(fp,"%d\n",&a[i][j]);
		} 
	}
	
	fclose(fp);
	for(i=0;i<N;i++){
		for(j=0;j<N;j++){
			printf("%d ",a[i][j]);
		}
		printf("\n");
	}
	printf("\n\n\n");

	for(i=0;i<N;i++){
		for(j=0;j<N;j++){
			if(a[i][j]!=0){
				choice[i][j][0] = 0;
			}
			else{
				choice[i][j][0] = N;
				for(int k=1;k<=N;k++){
					choice[i][j][k] = 1;
				}
			}
		}
	}
	BT(0,a);
	cout<<"num="<<num;
}
