print("請輸入顏色辭典，當key輸入end時結束")
dict1 = dict()
while True:
    key = input("Key:")
    if key == 'end':
        break
    value = input("Value: ")
    dict1[key] = value

for i in list(sorted(dict1.keys())):
    print(i,": ", dict1[i],sep='')
    