# 讀入使用者輸入的10個數字，存於List當中
numlist = list()
for i in range(1,11):
    temp = int(input("請輸入第"+str(i)+"個數字:"))
    numlist.append( temp )
    
print( numlist)

#分別計算每個數字出現的次數
numcount = list()
for i in range(10):
    numcount.append(numlist.count(numlist[i]))
    
print(numcount)


#列印出現最多次數的數字，以及出現次數

maxNumInput = numlist [numcount.index(max(numcount))]
print(maxNumInput,"出現最多次，共出現",max(numcount),"次")
