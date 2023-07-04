print ("請輸入數字,直到9999結束")

count = 1
while True:
    num = input("請輸入第"+str(count)+"個數字:")
    if num == '9999':
        break
    result = 0
    for i in range( len(num)-1,-1,-1):
        x = int(num[i])
        y = int(result)
        result = int(num[i]) + int(result)       
    print("數字加總為:",result)
    count += 1
print("您輸入的數字為9999，遊戲結束")



      