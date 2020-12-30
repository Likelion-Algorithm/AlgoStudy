from sys import stdin

croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = stdin.readline().strip()
count = 0

for i in range(len(croatia_alphabet)):
    num_alphabet = word.count(croatia_alphabet[i])
    if num_alphabet > 0:
        count += num_alphabet
        word = word.replace(croatia_alphabet[i], "1")

for j in range(len(word)):
    if word[j] != "1":
        count += 1

print(count)