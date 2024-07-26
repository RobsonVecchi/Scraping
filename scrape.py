from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import csv


def iniciar_driver():
    chrome_options = Options()

    arguments = ['--lang=pt-BR', 'window-size=800,600', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)
        
   
    driver = webdriver.Chrome(options=chrome_options)   
    return driver 


driver = iniciar_driver()
driver.get('http://books.toscrape.com/')
#You can change the category here to enrich the csv file. For testing, I did Psychology, History and Self Help.
psy = driver.find_element(By.LINK_TEXT, 'Self Help')
driver.execute_script("arguments[0].scrollIntoView();", psy)
sleep(2)
psy.click()
sleep(5)
count = 1
all_books = []
books_on_website = product_elements = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
sleep(5)
print("These are all the book: ")
print(books_on_website)
sleep(5)

for book in books_on_website:
    print(f"Doing book number {count}")
    sleep(2)
    title = book.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
    price = book.find_element(By.CSS_SELECTOR, "p.price_color").text
    availability = book.find_element(By.CSS_SELECTOR, "p.availability").text.strip()
    rating = book.find_element(By.CSS_SELECTOR, "p.star-rating").get_attribute("class").split()[-1]
    
    all_books.append({
            "Name": title,
            "Price": price,
            "Availability": availability,
            "Rating": rating
        })
    count+=1
print("Here are all the books: ")
print(all_books)
print("Printed!")

with open("product_data.csv", "a", newline="", encoding="utf-8") as csv_file:
        fieldnames = ["Name", "Price", "Availability", "Rating"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(all_books)
        
      
    