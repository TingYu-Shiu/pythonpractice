setAlpha = set(map(chr,range(97,123)))

print("請輸入句子以測試是否為全字母句，輸入end結束:")
while True:
    temp = input()
    if temp == "end":
       break
    set1 = set(temp.lower())
    if len (set1 & setAlpha) == 26:
        print("此句為全字母句")
    else:
        print("此句不是全字母句")
    
    