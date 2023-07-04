print("請輸入兩個正整數 a,b (a<=b)")
int1 = int(input("請輸入正整數(a):"))
int2 = int(input("請輸入正整數(b):"))

while True:
   if int1 <= int2 :
        count=0
        result=0
        for i in range(int1,int2+1):
             if i%7 == 0 or i%11 == 0:
               print("{:<4}".format(i),end=' ')
               count += 1
               result = result + i
               if count%10 ==0:
                print()
        break
   else:
       print("a需要<b,請重新輸入")
       int1 = int(input("請輸入正整數(a):"))
       int2 = int(input("請輸入正整數(b):"))
print()
print("總數共有",count,"個")
print("數字的總和是",result)
 
