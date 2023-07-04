import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules


# suport支持度，出現某元素(可以是同時出現)的比例 (10筆中有7筆同時買可樂跟薯片)
# confidence，一元素內包含另一特定元素的比例(9筆可樂中，同時有7筆買薯片)
# lift，a對於b的影響，同時出現兩項，比兩項單獨購買的機率相乘上升多少%


dataset = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
           ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
           ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs']]


te = TransactionEncoder()
te_ary = te.fit_transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
print(df)


result = apriori(df, use_colnames=True)
result['length'] = result['itemsets'].apply(lambda x: len(x))
print(result)

return_association_rule = association_rules(result, metric="support",min_threshold=0.2)

print(return_association_rule)
