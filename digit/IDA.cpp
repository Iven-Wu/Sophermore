#include<stdio.h>
#include<stdlib.h>
#include <iostream>
#define N 5
#define inf 10000
using namespace std;

typedef struct QNode{
    int data[N][N];
    struct QNode *father;
    int f;
    char how[5];
}QNode,*QueuePtr;

typedef struct linkList{
    QueuePtr content;
    struct linkList *next;
}linkList;
int target[N][N]={{1,2,3,4,5},{7,7,8,9,10},{6,7,11,12,13},{14,15,16,17,18},{19,20,21,0,0}};

bool isEqual(int a[N][N],int b[N][N]);
void printstate(int state[N][N]){
    for(int i = 0;i<N;i++){
        for(int j=0;j<N;j++){
            printf("%4d",state[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

void link(linkList *head,QNode *q){
	linkList *current = new linkList;
	current->content= q;
	current->next = head->next;
	head->next = current;
}
void copy(int a[N][N],int b[N][N]){     //b到a
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            a[i][j] = b[i][j];
        }
    }
}
bool in(linkList *head,int a[N][N]){

    linkList *current = head->next;

    while(current){
        if(isEqual(current->content->data,a)){
          return true;
        }
        current = current->next;
    }
    return false;
}
bool isEqual(int a[N][N],int b[N][N]){
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            if (a[i][j]!=b[i][j])
                return false;
        }
    }
    return true;
}
bool Delete(linkList *head,int index,QueuePtr &e){
    linkList *current = head;
    linkList *tmp;
    int i = 0;
    while( current&& i<index-1){
        current = current->next;
        i++;
    }
    tmp = current->next;
    e = current->next->content;
    current->next = tmp->next;
    free(tmp);
    return true;
}
int h(int now[N][N],int target[N][N]){
	int i,j,k;
	int count1 = 0;
	int count2 = 0;
	int ans = 0;
	int x1,y1,x2,y2;
	for(k=1;k<=21;k++){
		x1 = y1 = x2 = y2 = -1;
		if(k!=7){
			for(i=0;i<N;i++){
				for(j=0;j<N;j++){
					if(now[i][j]==k){
						x1 = i;
						y1 = j;
					}
					if(target[i][j]==k){
						x2 = i;
						y2 = j;
					}
				}
			}
		}
		else{
			for(i=0;i<N;i++){
				for(j=0;j<N;j++){
					if(now[i][j]==7){
						count1++;
						if(count1==2){
							x1 = i;
							y1 = j;
						}
					}
					if(target[i][j]==7){
						count2++;
						if(count2==2){
							x2 = i;
							y2 = j;
						}
					}
				}
			}
		}
		if(k!=7)
			ans +=abs(x1-x2)+ abs(y1-y2);
		if(k==7)
			ans +=3*(abs(x1-x2)+abs(y1-y2));
	}

	return ans*3;
}
int dir(int a[N][N],int x,int y){       //1表示7在这一格的上面 2表示下 3表示左 4表示右
                                          //14表示7在这一格的上面和右边
    if(x!=N-1 && a[x+1][y]==7)
        return 2;
    if(y!=0 && a[x][y-1]==7)
        return 3;
    if(y!=N-1 && x!=0 && a[x][y+1]==7 && a[x-1][y]==7)
        return 14;
    if(x!=0 && a[x-1][y]==7)
        return 1;
    if(y!=N-1 && a[x][y+1]==7)
        return 4;
    return 0;
}
int move(int a[N][N],int b[N][N],int count)      //移动 排除特殊情况
{
    //1 up 2 down 3 left 4 right
    int x1 = -1,y1 = -1;						//对于返回值
    int x2 = -1,y2 = -1;						// 0 表示不能动
    for(int i = 0;i < N;i ++){					// 1 2 3 4 表示单个格的上下左右
        for(int j = 0;j < N;j ++){
            b[i][j] = a[i][j];
            if( a[i][j]== 0 && x1 == -1) {
                x1 = i; y1 = j;
            }
            if(a[i][j]==0 && x1!=-1){
                x2 = i; y2 = j;
            }
        }
    }
    if (count==9){              //大7移动
        int m1 ,m2;
        m1=dir(a,x1,y1);
        m2=dir(a,x2,y2);
        int direction=-1;
        if(m1==14){             //两个方向取能动的方向
            if(m2==1)
                direction = 1;
            else if (m2==4)
                direction = 4;
        }
        if(m2==14){
            if(m1==1)
                direction = 1;
            else if (m1==4)
                direction = 4;
        }
        if((m1==m2 && m1!=0))
            direction = m1;
        if(direction!=-1){
            if(direction==1){
                b[x1-1][y1] = 0;
                b[x1][y1] = 7;
                b[x2-2][y2]=0;
                b[x2][y2] = 7;
                return 71;
            }
            else if(direction==2){
                b[x1][y1] = 7;
                b[x1+1][y1] =0;
                b[x2][y2] = 7;
                b[x2+2][y2] = 0;
                return 72;
            }
            else if(direction ==3){
                b[x1][y1] =7;
                b[x2][y2] = 7;
                b[x1][y1-2] = 0;
                b[x2][y2-1] = 0;
                return 73;
            }
            else if(direction ==4){
                b[x1][y1] = 7;
                b[x2][y2] = 7;
                b[x1][y1+2] = 0;
                b[x2][y2+1] = 0;
                return 74;
            }
        }
        else return 0;
    }
    else{                           //只移动一个的时候
        int x,y;
        if((count-1)/4==0){
            x = x1;
            y = y1;
        }
        else if((count-1)/4==1){
            x = x2;
            y = y2;
        }
        int dir = (count-1)%4+1;
        if(dir == 1){
            if(b[x-1][y]==7 ||b[x-1][y]==0|| x==0)
                return 0;
            b[x-1][y] = 0;
            b[x][y] = a[x-1][y];
            return 1+b[x][y]*10;
        }
        else if(dir == 2){
            if(b[x+1][y]==7 ||b[x+1][y]==0|| x==N-1)
                return 0;
            b[x+1][y] = 0;
            b[x][y] = a[x+1][y];
            return 2+b[x][y]*10;
        }
        else if(dir == 3){
            if(b[x][y-1]==7||b[x][y-1]==0 || y==0)
                return 0;
            b[x][y-1] = 0;
            b[x][y] = a[x][y-1];
            return 3+b[x][y]*10;
        }
        else if(dir == 4){
            if(b[x][y+1]==7 ||b[x][y+1]==0|| y==N-1)
                return 0;
            b[x][y+1] = 0;
            b[x][y] = a[x][y+1];
            return 4+b[x][y]*10;
        }
        else return 0;
    }

    return true;
}
void gethow(int how,QueuePtr &a){
	char temp[4];
	itoa(how/10,temp,10);
	//char ans[5];
	if(how%10==1){
    	sprintf(a->how,"(%s,u)",temp);
	}
	else if(how%10==2){
		//current->content->how[1] = 'd';
		sprintf(a->how,"(%s,d)",temp);
	}
	else if(how%10==3){
		//current->content->how[1] = 'l';
		sprintf(a->how,"(%s,l)",temp);
	}
	else if(how%10==4){
		//current->content->how[1] = 'r';
		sprintf(a->how,"(%s,r)",temp);
	}

}
void show(QueuePtr e){
	FILE *fp;
	fp = fopen("answer2.txt","w+");
	int k = 0;
	char *path[100] ;
	int step = 0;
    while(e){
		path[step++] = e->how;
		e = e->father;
    }
    printf("%d steps needed as follow:\n",step);
    step--;
    int stepforward = 1;
    for(;step>0;step--){
          fprintf(fp,"%s; ",path[step]);
          printf("step%d:",stepforward++);
          printf("%s;\n",path[step]);
    }
    fprintf(fp,"%s",path[step]);
    printf("step%d:",stepforward++);
    printf("%s",path[step]);
    fclose(fp);
}

int search(linkList *open,linkList *close,int g, int bound){
	QueuePtr node;
	//cout<<g;
	Delete(open,1,node);
	if(node->f>bound)
		return node->f;
	if(isEqual(node->data,target)){
		link(open,node);
		return -1;
	}
	link(close,node);
	int min = inf;
	for(int j=1;j<=9;j++){              //9种情况 前一个上下左右移 后一个 上下左右移 还有7上下左右移
        int tmp[N][N];                            //用来存储
        int m=move(node->data,tmp,j);
        if(m){					//cur 是要被扩展的结点
           if((!in(open,tmp))&&(!in(close,tmp))){      //判断是否出现过
                QueuePtr q = new QNode;
                copy(q->data,tmp);
                    //q->g = node->g+1;
                q->f = h(q->data,target) + g + 1;
                q->father = node;
                gethow(m,q);
                link(open,q);
                int t;
                t= search(open,close,g+1,bound);
                if(t==-1)
                    return -1;
                if (t<min)
                    min = t;
            }
        }
    }
    return min;
}
bool IDA(QNode *root){
	int bound = h(root->data,target);
	linkList *open = new linkList;
	linkList *close = new linkList;
	open->next = NULL;
	link(open,root);
	//QueuePtr cur = root;
	int nbound;
	while(1){
		int t;
		t =search(open,close,0,bound);
		if (t==-1){
			QueuePtr q = new QNode;
			Delete(open,1,q);
			show(q);
		}
		if (t==inf){
			cout<<"无解";
			return false;
		}

		bound = t;
	}
}
int main(){
	int i,j;
	FILE *fp;
	int start[N][N];
	//int target[N][N]={{1,2,3,4,5},{7,7,8,9,10},{6,7,11,12,13},{14,15,16,17,18},{19,20,21,0,0}};
	if((fp=fopen("2.txt","r+"))==NULL)
	{
		printf("cannot open");
		return 0 ;
	}
	for(i=0;i<N;i++){
		for(j=0;j<N;j++){
			fscanf(fp,"%d,\n",&start[i][j]);
		}
	}

	cout<<"start\n";
	printstate(start);
	printf("\n\n\n");

	cout<<"target\n";
	printstate(target);
	printf("\n\n\n");

	QueuePtr root = new QNode;
	copy(root->data,start);
	root->f = h(start,target);
	//root->g = 0;
	root->father = NULL;
    if(!IDA(root)){
        cout<<"无解";
        return 0;
    }
}
