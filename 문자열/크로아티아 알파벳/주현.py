string = list(input())
number = 0
for i in range(len(string)):
    if i ==1:
        if string[i] =='=':
            if string[0] in ['c','s','z']:
                number+=1
        elif string[i] =='-':
            if string[0] in ['c','d']:
                number+=1
        elif string[i] =='j':
            if string[0] in ['l','n']:
                number+=1
    elif i >1:
        if string[i] =='=':
            if string[i-1] in ['c','s','z']:
                if string[i-1]=='z' and string[i-2]=='d':
                    number+=1
                number+=1
        elif string[i] =='-':
            if string[i-1] in ['c','d']:
                number+=1
        elif string[i] =='j':
            if string[i-1] in ['l','n']:
                number+=1


      
print(len(string)-number)
