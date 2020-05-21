//201500787 김주현


#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#define SIZE  1000		//data의 size를 결정
#define TIMES  10		//해당 알고리즘을 몇 번 실행한 평균을 구할 지 결정


int savecompare=0;		//비교, 이동 횟수를 저장할 전역변수
int savemove=0;
int tc = 0;
int tm = 0;


void save(int com, int mov) {
	savecompare = com;
	savemove = mov;
}


void printSortPerf(int compare, int move) {
	printf("compare=%d\nmove=%d\n", compare, move);
}

//중복없는 무작위 원소를 갖는 배열 생성하는 함수
void setRandomSort(int a[],int n) {
	printf("%d개의 배열을 생성합니다\n", n);
	srand(time(NULL));
	for (int i = 0; i < n; i++) 
		{
		a[i] = rand() % SIZE;
			if(i >= 1)
			{
				for (int j = 0; j < i; j++)
				{
					if (a[j] == a[i])
					{
						a[i] = rand() % SIZE;
						j = -1;
					}
				}
			}
		}
}

//배열을 출력하는 함수
void printSort(int a[], int n) {
	printf("%d개의 배열을 출력합니다\n", n);
	int i;
	printf("{");
	for (i = 0; i < n - 1; i++)
	{
		printf("%d,", a[i]);
	}
	printf("%d}\n", a[n - 1]);

}

/*	해당 알고리즘을 TIMES번 실행한 비교,
	이동 횟수의 평균(성능)을 구하는 함수 */
void average(void(*pf)(int*m, int n), int a[], int f) {
	int count;
	for (count = 0; count < TIMES; count++)
	{
		_sleep(1000);
		setRandomSort(a, SIZE);
		(*pf)(a, f);
		tc += savecompare;
		tm += savemove;
		save(tc , tm );
		
	}
	printf("average of compare = %d\n", tc / TIMES);
	printf("average of move = %d\n", tm / TIMES);
	savecompare = 0;
	savemove = 0;
	tc = 0;
	tm = 0;
}

//매개변수가 다를 때
void averages(void(*pf)(int*m, int n,int g), int a[], int f, int h) {
	int tc = 0;
	int tm = 0;
	int count;
	for (count = 0; count < TIMES; count++)
	{
		_sleep(1000);
		setRandomSort(a, SIZE);
		(*pf)(a, f, h);
		tc += savecompare;
		tm += savemove;
		save(tc, tm);

	}
	printf("average of compare = %d\n", tc / TIMES);
	printf("average of move = %d\n", tm / TIMES);
	savecompare = 0;
	savemove = 0;
	tc = 0;
	tm = 0;
}



void swap(int a[],int i, int min) {
	int x;
	x = a[i];
	a[i] = a[min];
	a[min] = x;
}

//각각의 정렬 알고리즘 구현
void selectionSort(int a[], int n) {
	int compare = 0;
	int move = 0;
	int* pcompare;
	int* pmove;
	pcompare = &compare;
	pmove = &move;
	int i, j, min;
	for (i = 0; i < n - 1; i++)
	{
		min = i;
		for (j = i + 1; j < n; j++)
		{
			if (a[j] < a[min])
			{
				min = j;
			}
			compare++;
		}
		if (i != min)
		{
			swap(a, i, min);
			move += 2;
		}
	}
		printSortPerf(compare, move);
		save(compare, move);
}

void bubbleSort(int a[], int n) {
	int compare = 0;
	int move = 0;
	int i, j;
	for (i = n - 1; i >= 0; i--)
	{
		for (j = 0; j < i; j++)
		{
			if (a[j] > a[j + 1])
			{
				swap(a, j, j + 1);
				move += 2;
			}
			compare++;
		}
	}
	printSortPerf(compare, move);
	save(compare, move);
}


void insertionSort(int a[], int n) {
	int compare = 0;
	int move = 0;
	int i, val, pos;
	for (i = 1; i < n; i++)
	{
		val = a[i];
		for (pos = i; pos > 0; pos--)
		{
			compare++;
			if (val < a[pos - 1])
			{
				a[pos] = a[pos - 1];
				move++;
			}
			else
			{
				break;	
			}
		}
		if(a[pos]!=val)
		{
			a[pos] = val;
			move++;
		}
	}
	printSortPerf(compare, move);
	save(compare, move);

}

void insertionSort2(int a[], int first, int last, int h, int* pcompare, int* pmove) {
	int i, val, pos;
	
	for (i = first + h; i <= last; i += h)
	{
		val = a[i];
		for (pos = i; pos > first; pos -= h)
		{
			*pcompare+=1;
			if (val < a[pos - h])
			{
				a[pos] = a[pos - h];
				*pmove+=1;
			}
			else
				break;
		}
		if (a[pos] != val)
		{
			a[pos] = val;
			*pmove += 1;
		}
	
	}
}
void shellSort(int a[], int n) {
	int i, h;
	int compare=0;
	int move=0;
	int* pcompare;
	int* pmove;
	pcompare = &compare;
	pmove = &move;
	for (h = n / 2; h > 0; h = h / 2)
	{
		for (i = 0; i < h; i++)
		insertionSort2(a, i, n - 1, h, pcompare, pmove);
	}
	printSortPerf(compare, move);
	save(compare, move);
}

void merge(int a[], int fstp, int sndp, int trdp, int fthp, int* pcompare, int* pmove) {
	int b[SIZE];
	int fst = fstp;
	int set = fstp;
	while ((fstp <= sndp) && (trdp <= fthp))
	{
		*pcompare += 1;
		if (a[fstp] <= a[trdp])
		{
			b[set] = a[fstp];
			fstp++;
			set++;
			*pmove += 1;
		}
		else
		{
			b[set] = a[trdp];
			trdp++;
			set++;
			*pmove += 1;
		}

	}
	if (fstp > sndp)
	{
		for (int j = trdp; j <= fthp; j++)
		{
			b[set] = a[j];
			set++;
			*pmove += 1;
		}
	}
	if (trdp > fthp)
	{
		for (int k = fstp; k <= sndp; k++)
		{
			b[set] = a[k];
			set++;
			*pmove += 1;
		}
	}
	for (int i = fst; i <= set - 1; i++)
	{
		a[i] = b[i];
		*pmove += 1;
	}
}

void mergeSort(int a[],int m,int n) {
	static int compare = 0;
	static int move = 0;
	static int* pcompare;
	static int* pmove;
	pcompare = &compare;
	pmove = &move;
	if((n-m) >= 1) 
	{
		int mid =(m + n) / 2;		
		mergeSort(a, m, mid);
		mergeSort(a, mid + 1, n);
		merge(a, m, mid, mid + 1, n, pcompare, pmove);
	}
	if (n - m + 1 == SIZE)
	{
		printSortPerf(compare - savecompare, move - savemove);
		save(compare - savecompare, move - savemove);
	}
}

int partition(int a[], int begin, int end, int*pcompare, int*pmove) {
	int pivot = begin;
	int L = begin;
	int R = end;
	while (L < R)
	{
		
		while (a[L] <= a[pivot] && L < end)
		{
			L++;
			*pcompare +=1;
		}
		while (a[R] > a[pivot])
		{
			R--;
			*pcompare +=1;
		}
		if (L < R) 
		{
			swap(a, L, R);
			*pmove +=2;
		}
	}	if (a[pivot] != a[R])
		{
		swap(a, pivot, R);
		*pmove += 2;
		}
	return R;
	}

void quickSort(int a[], int begin, int end) {
	static int compare = 0;
	static int move = 0;
	static int* pcompare;
	static int* pmove;
	int pivot;
	pcompare = &compare;
	pmove = &move;
	if (begin < end) 
	{
		pivot = partition(a, begin, end,pcompare,pmove);
		quickSort(a, begin, pivot - 1);
		quickSort(a, pivot +1, end);
	}
	
	if (end - begin + 1 == SIZE)
	{
		printSortPerf(compare-savecompare,move-savemove);
		save(compare - savecompare, move - savemove);
	}
	
}


int main() {
	int a[SIZE];
	//a,SIZE를 매개변수로 하는 알고리즘의 성능		:  average
	//a,begin,end를 매개변수로 하는 알고리즘의 성능 : averages

	
	//average(selectionSort, a, SIZE);
	
	//average(bubbleSort,a,SIZE);
	
	//average(insertionSort,a,SIZE);
	
	//average(shellSort,a,SIZE);
	
	//averages(mergeSort,a,0,SIZE-1);
	
	//averages(quickSort,a,0,SIZE-1);

	//setRandomSort(a, SIZE);
	
	//printSort(a,SIZE);
	
	//selectionSort(a,SIZE);

	//bubbleSort(a, SIZE);

	//insertionSort(a, SIZE);

	//shellSort(a, SIZE);

	//mergeSort(a, 0, SIZE - 1);

	//quickSort(a, 0, SIZE-1);

	//printSort(a, SIZE);

	return 0;
}