import numpy as np
import pandas as pd
random_number = np.random.randint(1,5,size = 2000)
print(random_number)
product =(['milets','milk','bread','butter','detergent']) 
random_product = np.random.choice(product,size = 2000)
branch = (['Mayiladuthurai','Thanjavur','Trichy','Nagapattinam','Kumbakonam'])
random_branch = np.random.choice(branch,size = 2000)
df = pd.DataFrame({
    'randomnumbers': random_number,
    'product': random_product,
    'branch' : random_branch
})
df.to_csv("random.csv",index =False)
print("CSV file saved!!!")
