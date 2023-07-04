def primeTest(n):
        x=0
        if n <= 1:
          return str(n)+"為非質數"
        else:
            for i in range(2,n):
              if n%i==0:
                  x += 1
            if x>0 :
              return str(n)+"為非質數"
            elif x == 0 or n==2:
              return str(n)+"為質數" 
            
while True  :             
  a= int(input("請輸入一整數 a:"))
  if a == -9999:
      break
  print(primeTest(a))
  
  
        

