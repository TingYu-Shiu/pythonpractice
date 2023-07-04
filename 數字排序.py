numlist = list()
for i in range(1,11):
    temp = int(input("請輸入第"+str(i)+"個數字:"))
    numlist.append( temp )
    
print(numlist)

i = 0
max2 = list()
while i< 3:
    max2.append(max(numlist))
    numlist.pop(numlist.index(max(numlist)))
    i += 1
   

j = 0
min3 = list()
while j < 3:
    min3.append(min(numlist))
    numlist.pop(numlist.index(min(numlist)))
    j += 1
    
min3.sort(reverse=True) 

print("最大三個數:",max2)
print("最小三個數",min3)
