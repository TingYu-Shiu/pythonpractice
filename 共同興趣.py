set1 = set(input("請輸入A的興趣").split(' '))
set2 = set(input("請輸入B的興趣").split(' '))

print("A與B所有的興趣:",sorted(set1|set2))
print("A與B共同的興趣:",sorted(set1&set2))
print("A與B彼此沒有的興趣:",sorted(set1^set2))
print("A有但B沒有的興趣:",sorted(set1-set2))