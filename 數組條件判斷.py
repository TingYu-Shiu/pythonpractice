list1 = input("請輸入一連串字串,中間以空白做分隔:").split(" ")
tuple1 = tuple(list1)

tuple2 = tuple1[0:3]

list2 =list()
for i in range (3):
    value = list1.pop()
    list2.append(value)

list2.reverse()

print("前三個:",tuple2,sep='')
print("後三個:",tuple(list2),sep='')

