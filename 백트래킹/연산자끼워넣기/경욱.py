import sys
num = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().split()))
add_num,sub_num,mul_num,div_num = list(map(int,sys.stdin.readline().split()))
result_list = []
def DFS(num,depth,add,sub,mul,div,result):
    if num== depth+1:
        result_list.append(result)
    else:
        if add:
            DFS(num,depth+1,add-1,sub,mul,div,result+num_list[depth+1])
        if sub:
            DFS(num,depth+1,add,sub-1,mul,div,result-num_list[depth+1])
        if mul:
            DFS(num,depth+1,add,sub,mul-1,div,result*num_list[depth+1])
        if div:
            if result <0:
                
                temp = -(abs(result) //num_list[depth+1])
                DFS(num,depth+1,add,sub,mul,div-1,temp)    
            else:
                DFS(num,depth+1,add,sub,mul,div-1,result//num_list[depth+1])
    
DFS(num,0,add_num,sub_num,mul_num,div_num,num_list[0])


print(max(result_list))
print(min(result_list))






import sys
num = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().split()))
add_num,sub_num,mul_num,div_num = list(map(int,sys.stdin.readline().split()))
# check_list   = ['+',False]*add_num  ['-',False]*sub_num +['*']*mul_num +['/']*div_num 
check_list=[]
for _ in range(add_num):
    check_list.append(['+',False])
for _ in range(sub_num):
    check_list.append(['-',False])
for _ in range(mul_num):
    check_list.append(['*',False])
for _ in range(div_num):
    check_list.append(['/',False])    

result_list =[ㅊ]
result = num_list[0]
def DFS(num,depth,check_list,num_list,result):
    # print(result,check_list, depth)
    
    if depth+1 == num:
        result_list.append(result)
        return
   
    else:
        for i in range(len(check_list)):
            if check_list[i][1]==False:
                if check_list[i][0]=='+':
                    check_list[i][1]=True
                    result += num_list[depth+1]
                    DFS(num,depth+1,check_list,num_list,result)
                    result -=num_list[depth+1]
                    check_list[i][1] = False
            
                if check_list[i][0]=='*':
                    check_list[i][1]=True
                    result *= num_list[depth+1]
                    DFS(num,depth+1,check_list,num_list,result)
                    result = result // num_list[depth+1]
                    check_list[i][1] = False
                
                if check_list[i][0]=='-':
                    check_list[i][1]=True
                    result -= num_list[depth+1]
                    DFS(num,depth+1,check_list,num_list,result)
                    result +=num_list[depth+1]
                    check_list[i][1] = False
            
                if check_list[i][0]=='/':
                    check_list[i][1]=True
                    if result <0:
                        temp=result
                        result = -(abs(result) //num_list[depth+1])
                        DFS(num,depth+1,check_list,num_list,result)
                        result = temp
                        check_list[i][1] = False
                    else:
                        result //= num_list[depth+1]
                        DFS(num,depth+1,check_list,num_list,result)
                        result = result * num_list[depth+1]
                        check_list[i][1] = False
    
DFS(num,0,check_list,num_list,result)


print(max(result_list))
print(min(result_list))

