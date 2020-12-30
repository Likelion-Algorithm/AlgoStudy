import sys

alphabetlist = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=' ,'z=']
word = sys.stdin.readline().rstrip()
wordlen = len(word)
checker = [0]*len(word)

for i in range(len(alphabetlist)):
    target = alphabetlist[i]
    target_len = len(target)
    for j in range(len(word)-(target_len-1)):
        compare = word[j:j+target_len]

        if target == compare and sum(checker[j:j+target_len]) == 0:
            wordlen-= (target_len-1)
            for k in range(j, j+target_len):
                checker[k] = 1
        else:
            continue
print(wordlen)

#통과