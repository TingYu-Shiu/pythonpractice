print ("請輸入數字,直到9999結束")

count = 1
while True:
    num = input("請輸入第"+str(count)+"個數字:")
    if num == "9999":
        break
    result = " "
    for i in range( (len (num)),0,-1 ):
        result = num[i] + result
    print("數字加總為:",result)
    count += 1
print("您輸入的數字為9999，遊戲結束")