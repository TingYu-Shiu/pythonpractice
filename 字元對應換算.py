list1 = list(input("請輸入一個字串:"))

for i in list1:
    print("ASCII code for {} is {}".format(i,ord(i)))
    
print(sum(map(ord, list1)))