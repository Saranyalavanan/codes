import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

df = pd.read_csv("datasets/realistic_grocery_transactions.csv")
transactions = df["Items"].apply(lambda x: [item.replace('_', ' ') for item in x.split(',')])

te = TransactionEncoder()
te_array = te.fit_transform(transactions)
df_encoded = pd.DataFrame(te_array, columns=te.columns_)
print(df_encoded)

freq = apriori(df_encoded, min_support=0.01, use_colnames=True) 
rule = association_rules(freq, metric="lift", min_threshold=1)

print(rule[["antecedents", "consequents", "support", "lift"]]
      .sort_values(by="lift", ascending=False))

