import pandas as pd
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup as bs
from tabulate import tabulate

from time import sleep
from time import time
from random import randint

desc=[]
physical=[]
specs=[]
prices=[]
database=[]

start_time = time()
requests = 0

mainUrl = "https://www.flipkart.com/laptops/pr?page="
pageNumber=1
nextUrl = "&sid=6bo%2Cb5g&viewType=list"

def get_url(mainUrl , pageNumber , nextUrl):
    return mainUrl + str(pageNumber) + nextUrl

def getpage(url):
    try:
        page = urlopen(url)
    except HTTPError as e:
        return None
    
    return page
    
def calc_laptops_page(desc , physical , specs , prices):
    laptops = []
    for i in range(len(desc)):
        laptop=[]
        laptop.append(desc[i])
        laptop.append(physical[i])
        laptop.append(prices[i])
        laptop.append(specs[i])
        laptops.append(laptop)  
        
    return laptops
    
def print_table(laptops):
        print(tabulate( laptops , headers=["Description" ,"Physical" ,"Prices"])) 
    
def extract_data(bsObj):
    table = bsObj.select("._2-gKeQ")

    for col in table:
        laptop_col = col.select("._1-2Iqu")[0]
    
        laptop_desc_col = laptop_col.select("._3wU53n")[0]
        laptop_desc = laptop_desc_col.string
        desc.append(laptop_desc)
    
        laptop_phy_col = laptop_col.select(".OiPjke")[0]
        laptop_phy = laptop_phy_col.string
        physical.append(laptop_phy)
    
        laptop_specs_cols=laptop_col.select(".tVe95H")
        laptop_specs=[]
        for laptop_specs_col in laptop_specs_cols:
            laptop_specs.append(laptop_specs_col.string)
            specs.append(laptop_specs)
        
        
        price_col = laptop_col.select("._2rQ-NK")[0]
        laptop_price = price_col.get_text()
        prices.append(laptop_price)  
        
def extract_data_multiple_pages(pages):
    requests = 0
    for i in range(pages):
        #print("PAGE" + str(i+1))
        #print("_______________________________________________________________________________________________________________________________")
        
        url = get_url(mainUrl , i+1 , nextUrl)
        page = getpage(url)

        sleep(randint(8,15))
        requests += 1
        elapsed_time = time() - start_time
        print('Request:{}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))

        if page.status != 200:
            warn('Request: {}; Status code: {}'.format(requests, response.status_code))

        if requests > 72:
            warn('Number of requests was greater than expected.')  
            break 

        if page==None:
            print("Error reading page")
    
        html = page.read()
        bsObj = bs(html , "lxml")

        extract_data(bsObj)

#print(bsObj.prettify())


        laptops = calc_laptops_page(desc , physical , specs , prices)
        #print_table(laptops)
        database.append(laptops)
        
       
if __name__ == "__main__":
    extract_data_multiple_pages(5)
    #print(database[0])
    f= open("laptop_data.txt" , "w")
    
    for page in database:
        for laptop in page:
            f.write("   %s\n" % "Description of laptop")
            f.write("           %s\n" %laptop[0])
            
            f.write("   %s\n" % "Physical specs")
            f.write("       %s\n" % laptop[1])
            
            f.write("   %s\n" % "Specs of laptop")
            for spec in laptop[3]:
                f.write("       %s\n" % spec)
                
            
            f.write("   %s\n" % "Price of laptop")
            f.write("       %s\n" % laptop[2])
            
            f.write("%s" %"\n\n\n\n\n")            
            
            
            
                
    
    
    
    
                    
    
    




    
    
     
        
        
    
    
    
    
    
    
    



