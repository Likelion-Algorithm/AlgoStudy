# ✏️ **알고리즘 스터디 위키** ✏️
<br/>
알고리즘 문제를 풀면서 눈여겨볼 만한 입·
출력 양식이나<br/>   
모듈·메소드 또는 알고리즘 내용을 기록합니다.<br/>
<br/>
목차 변경시에는 갱신을 부탁드입니당.😗<br/>

[TOC generator](https://ecotrust-canada.github.io/markdown-toc/) (한글작성 시 미동작. 참고만)


<br/>   

## **📚 목차**
#
<br/> 

- [**PYTHON**](#python)

  * [**1. 입력**](#1-입력)
  * [**2. 출력**](#2-출력)
  * [**3. 모듈**](#3-모듈)

- [**알고리즘**](#알고리즘)

<br/>
<br/>

#
<br/>

# **PYTHON**
<br/>
<br/>

## **1. 입력**
<br/>

----
* ### input() &  sys.stdin.readline()
입력받는 방법에는 크게 두 가지가 있다.  
input()과 sys.stdin.readline()인데,   
input()은 내장함수로 바로 사용할 수 있고  
sys.stdin.readline()은 sys모듈을 import해야하는 차이가 있다.  
동작 방식도 약간 차이가 있으며, 성능도 후자가 우세하여  
보통 sys.stdin.readline()을 권장한다.  

(그러나 개인적으로 입력 차이로 틀리는 문제는 아직 못봤다.)

------
* ### 여러 문자 한번에 입력받기  
백준은 보통 공백을 기준으로 나눠진 수를 입력받는다.  
map함수와 split함수를 이용해 다음과 같이 한 번에 받을 수 있다.
>a=1, b=2, c=3 인 입력이  
1 2 3  
으로 들어올때 

    a, b ,c= map(int, input().split())
------
* ### N차원 배열 입력
 앞의 내용처럼 공백문자로 구분 된 입력을 각각의 변수로 받을 수도 있지만,  
 list 함수를 이용하면 배열로 만들 수 있다.
 >1 1 1 1 1 -> [1, 1, 1, 1, 1]  

    array = list(map(int,input().split()))
<br/>

>6 6  #(row, column)  
1 1 1 1 1 1  
1 0 0 0 0 1  
1 0 1 1 1 1  
1 0 1 1 1 1  
1 0 1 1 1 1  
1 1 1 1 1 1 

```python
row, column =  map(int, input().split())
array = []
for i in range(row):
array.append(list(map(int, input().split())))
```
```python
row, column =  map(int, input().split())
array = [list(map(int, input().split())) for r in range(row)]
print(array)
#list comprehension
```    

## **2. 출력**
<br/>

## **3. 모듈**
<br/>


<br/>
<br/>
<br/>

# **알고리즘**
