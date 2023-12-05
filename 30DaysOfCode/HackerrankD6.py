n = int(input())
dizi=[]

i=0
j=0
k=0
for i in range(0,n):
 STDIN = input()
 dizi.append(STDIN)

for k in range(0,n):
    for j in range(0,len(dizi[k]),2):
        print(dizi[k][j],end='')
    print(end=' ')
    for j in range(1,len(dizi[k]),2):
        print(dizi[k][j],end='')
    print()
