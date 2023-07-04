print("請輸入數字，直到9999結束")

count = 1 
maximum = int(input("請輸入第"+str(count)+"個數字:"))
userInput = maximum
while userInput != 9999:
      if userInput > maximum:
          maximum = userInput
      count +=1
      userInput = int(input("請輸入第"+str(count)+"個數字:"))
print("輸入的最大值為",maximum)