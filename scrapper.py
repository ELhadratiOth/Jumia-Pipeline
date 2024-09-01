from bs4 import BeautifulSoup
import pandas as pd
import requests
from configparser import ConfigParser


config  = ConfigParser()
config.read('config.ini')
searched_product = config['SEARCH_TARGET']['serched_product']

products = []
cleaning_patterns = ['Pochette' , 'Mirror' , 'etui' , 'Chargeur' , 'Wireless' , 'Coque' , 'Cover']
for i in range(10):
          print("page : " , i)
          LINK = f"https://www.jumia.ma/catalog/?q={searched_product}&page={i}#catalog-listing"
          r = requests.get(LINK)
          # print(r.status_code)
          # print(r.content)
          soup = BeautifulSoup(r.content, "html.parser")
          data = soup.find_all("article" , attrs={"class": "c-prd"})
          # print(len(data))
          for prod in data:
                    dic= {}
                    dic['product_name'] = prod.find('h3').contents[0]
                    
                    price = prod.find('div' , attrs={'class' : 'prc'}).contents[0].split(' ')[0].split(',')
                    dic['product_price'] = float(''.join(price))
                    
                    dic['product_link'] = "https://www.jumia.ma" + prod.find('a' , attrs={'class' : 'core'})['href']
 
                    if not any( elem.lower() in dic['product_name'].lower() for elem in cleaning_patterns ) and dic['product_price']> 500  :
                              products.append(dic)        

# print(products[-1])


df = pd.DataFrame.from_records(products) 
df.to_csv(f"{searched_product}.csv" , index=False)
# print(df.head)
                    
          
          
          