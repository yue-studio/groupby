from faker import Faker
import random
import json
import pandas as pd
import numpy as np

#
# generate 100 random users
# 
def gen_users(users):
   fake = Faker()            # for fake name

   phone_brands = ['Apple', 'Samsung','NA']
   apple_phones = ['iPhone X', 'iPhone 7']
   samsung_phones = ['Galaxy 4', 'Galaxy 5']

   for i in range(100):
      brand = random.choice(phone_brands)

      if brand == 'Apple':
         phone = random.choice(apple_phones)
      elif brand == 'Samsung':
         phone = random.choice(samsung_phones)
      else:
         phone = 'None'

      users.append({"name":fake.name(), "age":random.randint(1,110), "brand":brand, "phone":phone })
  

#
# main routine to summarize the data
#
def main():
   users = []
   gen_users(users)
   df = pd.DataFrame.from_dict(users, orient='columns')
   z = df.groupby([pd.cut(df.age,bins=np.arange(0,110,10)), 'brand']).brand.size()

   print z 

if __name__== "__main__":
  main()
