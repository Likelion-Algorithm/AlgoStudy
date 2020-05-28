# if "ab">"ac":
#     print(True)
# elif "ab"<'ac':
#     print(False)

# if [1,-1] >[1,1]:
#     print(True)
# if [1,-1] <[1,1]:
#     print(False)


# if  "ab">"ac":
#     print(True)
# if "ab"<"ac":
#     print(False)

if '21 Junkyu' >'21 Dohyun':
    print(True)
if '21 Junkyu' < '21 Dohyun':
    print(False)
if '21 Junkyu' == '21 Dohyun':
    print('hooo')



a = '21 Junkyu'.split()[0]
b = a
print(b)

def quick_sort(data_list):
    if len(data_list)<=1:
        return data_list
    left,right = list(),  list()
    pivot = data_list[0]
    for index in range(1,len(data_list)):
        if int(pivot.split()[0]) > int(data_list[index].split()[0]):
            left.append(data_list[index])
        else:
            right.append(data_list[index])
    return quick_sort(left) + [pivot] + quick_sort(right)



import sys
num_input = int(sys.stdin.readline())
member_list = list()
for i in range(num_input):
    member_list.append(sys.stdin.readline().strip())

for i in quick_sort(member_list):
    print(i)