#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#define LENGTH 10
#define ROWS 2
#define LEN 3

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
int add(int a,int b){
	int c;
	c = a + b;
	return c;
}

int fi(int n){
	int k = 1,i;
	for (i = n;i >= 1; i--){
		k = k * i;
	}
	return k;
}

int fir(int n){
	if (n == 1){
		return 1;
	}else{
		return n * fir(n - 1);
	}	
}

int gcd(int m,int n){
	if (n == 0){
		return m;
	}else{
		return gcd(n,m % n);
	}
}

int fibo(int n){
	if (n == 0){
		return 0;
	}else if(n == 1){
		return 1;
	}else{
		return fibo(n-1) + fibo(n-2) ;
	}
}

int main(int argc, char *argv[]) {
	
	printf("%d \n",fibo(8));
	//printf("%d\n",gcd(20,14));
	
	
	/*int ans = fi(5);
	printf("5!: %d \n",ans);
	int ans2 = fir(5);
	printf("5!: %d \n",ans2);*/
/*	
	int m = 6 ,n = 2;
	int c;
	c = add(m,n);
	printf("%d\n",c);
	c = add(7,3);
	printf("%d\n",c);*/
	
/*	int ans,gus;
	srand(time(0));
	ans = (rand()%5) + 1;
	printf("1-5�q�@�ӼƦr:");
	scanf("%d",&gus);
	
	if (gus == ans){
		printf("�q��F\n");
	}else{
		printf("�q���F\n");
	}*/
	
	
	/*float x,y,z;
	printf("��J����:");
	scanf("%f",&x);
	printf("��J����:");
	scanf("%f",&y);
	z = sqrt(pow(x,2) + pow(y,2));
	printf("�����:%.2f",z);*/
	
	
	/*
	1 4
	2 5
	3 6
	*/
	/*int arra2x3[ROWS][LEN] = {{1,2,3},
							  {4,5,6}};
	int i ,j;
	for (i = 0; i <LEN ;i++){
		for ( j = 0 ; j < ROWS;j++){
			printf("%d ",arra2x3[j][i]);
		}
		printf("\n");
	}*/	
	
	/*int arra2x3[ROWS][LEN] = {{1,2,3},
							  {4,5,6}};
	int i ,j;
	for (i = 0; i < ROWS;i++){
		for ( j = 0 ; j < LEN;j++){
			printf("%d ",arra2x3[i][j]);
		}
		printf("\n");
	}*/							  
	
	
	/*int number[5] = {0,1,2,3,4};
	int length = sizeof(number)/sizeof(number[0]);
	int i;
	for (i = 0; i < length;i++){
		printf("%d ",number[i]);
	}
	printf("\n");*/
	
	
	
	/*int arr[LENGTH] = {0};
	int i;
	for ( i = 0; i < LENGTH;i++){
		printf("%d ",arr[i]);
	}
	printf("\n");
	for (i = 0; i < LENGTH;i++){
		arr[i] = i;
	}
	printf("\n");
	for (i = 0; i < LENGTH;i++){
		printf("%d ",arr[i]);
	}
	printf("\n");*/
	
/*	int input = 0;
	
	do{
		printf("��J�@�ө_��:");
		scanf("%d",&input);
		if (input % 2 != 0){
			printf("�_��\n");
			break;
		}
		printf("�b�դ@��!\n");		
	}while(1);*/
	


/*	int score = 0;
	int sum = 0;
	int count = 0;
	int i = 0;
	
	for (i = 0; i < 5; i++){
		printf("��J����:");
		scanf("%d",&score);
		if (score < 0 || score > 100){
			printf("���ƿ��~");
			continue;
		}
		count++;
		sum += score;
	}
	printf("�`���Z%d\n",sum);
	printf("����%.2f\n",(float)sum/count);*/
	

/*	int i = 0;
	for ( i = 1; i< 10;i++){
		if (i == 3){
			break;
		}
		printf("%d ",i);
	}
	
	printf("\n");
	for ( i = 1; i< 10;i++){
		if (i % 2 == 0){
			continue;
		}
		printf("%d ",i);
	}*/
	
/*	int input = 0;
	int replay = 0;
	
	do{
		printf("�п�J���:");
		scanf("%d",&input);
		printf("�O�_���_��?%c\n",(input %2)?'Y':'N' );
		printf("1�~�� 0:����");
		scanf("%d",&replay);				
	}while(replay);*/
	
	
/*	int score = 0;
	int sum = 0;
	int count = -1;
	
	while(score != -1){
		count++;
		sum += score;
		printf("��J���Z-1����");
		scanf("%d",&score);
	}
	printf("������:%.2f\n",(float)sum / count);*/
	
	/*int i,j;
	for (i = 2; i < 10;i++){
		for (j = 1; j < 10 ;j++){
			printf(" %d * %d=%2d",i,j,i*j);
		}
		puts("");
	}*/
	
	
	/*int i;
	for (i = 0; i < 10; i++){
		printf("%d \n",i); 
	}*/
	
	/*int action = 0;
	printf("�п�J�ʧ@\n");
	printf("1 �}�l\n");
	printf("2 ���}\n");
	printf("3 �Ȱ�\n");
	scanf("%d",&action);
	switch(action){
		case 1:
		 puts("�}�l");
		break;
		case 2:
		 puts("���}");	
		break;
		case 3:
		  puts("�Ȱ�");	
		break;
		default:
		  puts("���~");	
	}*/
	
/*	int score = 0;
	printf("�п�J���Z:");
	scanf("%d",&score);
	if (score >= 90){
		puts("A");
	}else if(score >= 80 && score < 90){
		puts("B");
	}else if(score >= 70 && score < 80){
		puts("C");	
	}else if(score >= 60 && score < 70){
		puts("D");	
	}else{
		puts("F");	
	}*/
	
/*	int input = 0;
	int remain = 0;
	printf("��J���:");
	scanf("%d",&input);
	remain = input % 2;
	if (remain == 1){
		printf("�_��");
	}else{
		printf("����");
	}*/
	
	/*int score = 65;
	printf("�O�_�ή�?%c\n",score >= 60 ?'Y':'N');*/
	
/*	int input = 0;
	printf("��J���:");
	scanf("%d",&input);
	
	printf("�O�_���_��?%c\n",input % 2 ? 'Y' : 'N');*/

	
	/*char str[20];
	puts("��J�r��:");
	gets(str);
	
	puts("�ڿ�J���r��:");
	puts(str);*/

/*	char c;
	printf("��J�r��:");
	c = getchar();
	putchar(c);
	putchar('\n');*/
	
	
	/*
	int input1;
	printf("�п�J���:");
	scanf("%d",&input1);
	printf("input1:%d",input1);*/
	
	
	/*printf("Hello\n");
	printf("%c\n",'A');
	printf("%5d\n",25);
	printf("%.2f\n",2.71828);
	int a = 10;
	int b = 20;
	printf("%d + %d = %d \n",a,b,a + b);*/

	
	return 0;
}
