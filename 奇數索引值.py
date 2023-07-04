x = []


for i in range(1,11):
    number = input("請輸入第"+str(i)+"個數字:")
    x.append(number)


result = int(x[1])+int(x[3])+int(x[5])+int(x[7])+int(x[9])
   
print("奇數索引數值總合為:",result)               