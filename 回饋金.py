
while True:
    i = int(input("輸入購買總價:"))
    if i == 0:
        break
    
    arr = [400,200,100,0]
    rat = [0.03,0.05,0.075,0.1]
    r=0
    
    for j in range(0,4):
        if i > arr[j]:
            r += (i-arr[j])*rat[j]
            i= arr[j]
    print("總優惠金額:",r,"元")
        
