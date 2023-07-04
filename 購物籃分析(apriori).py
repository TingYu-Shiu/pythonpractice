from apyori import apriori

 
data = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
           ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
           ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs']]


# suport支持度，出現某一元素的比例
# confidence，出現一元素後會購買另一特定元素的比例
# lift，a對於b的影響，比兩項單獨購買的機率相乘上升多少%

association_rules = apriori(data, min_support=0.16, min_confidence=0.2, min_lift=1.5, max_length=2) 
association_results = list(association_rules)
 
for item in association_results:
   pair = item[0] 
   items = [x for x in pair] #要用for loop跌代出來
   print("Rule: " + items[0] + " -> " + items[1])
   print("Support: " + str(item[1]))
   print("Confidence: " + str(item[2][0][2]))
   print("Lift: " + str(item[2][0][3]))
   print("=====================================")
