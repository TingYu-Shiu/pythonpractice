import datetime

starttime = datetime.datetime.now() #開始計算時間
##############
 
for i in range(1000):
    for j in range(1000):
        continue
    print('test ' ,end='')
##############
print('')
endtime = datetime.datetime.now() #結束時間
print(endtime - starttime) #程式執行時間