# Task 1 Initiate the driver

# Task 2 Load flipkart.com

# Task 3 In search bar seach for 'Samsung Galaxy S10'

# Task 4 On results page click on 'Mobiles' in categories

# Task 5 Apply the filters by selecting Brand as SAMSUNG and selecting Flipkart asssured

# Task 6 Select the option 'Price -> High to Low'

# Task 7 Get only the 1st Page of the resullts

# Task 8 Print the list of Product Name, Display Price, Link to Product Details Page for each result in results

# Importing the modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# T1 Initiate the driver
driver = webdriver.Chrome()

# T2 Load flipkart.com
driver.get("https://www.flipkart.com/")

# T3 In search bar search for 'Samsung Galaxy S10'
mobile_search = driver.find_element(By.NAME, "q")
mobile_search.send_keys("Samsung Galaxy S10")
mobile_search.send_keys(Keys.RETURN)

# T4 On results page click on 'Mobiles' in categories'
mobiles_category = driver.find_element(By.XPATH, "//a[text()='Mobiles']")
mobiles_category.click()

# T5 Apply the filters by selecting Brand as SAMSUNG and selecting Flipkart asssured
samsung_filter = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[text()='SAMSUNG']"))
)
driver.execute_script("arguments[0].click();", samsung_filter)
time.sleep(2)

flipkart_assured_filter = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//img[contains(@src, 'fa_62673a.png')]"))
)
#driver.execute_script("arguments[0].scrollIntoView(true);", flipkart_assured_filter)
driver.execute_script("arguments[0].click();", flipkart_assured_filter)
time.sleep(2)

# T6 Select the option 'Price -> High to Low'
sort_high_to_low = driver.find_element(By.XPATH, "//div[text()='Price -- High to Low']")
sort_high_to_low.click()

# T7 Get only the 1st Page of the resullts
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "_75nlfW"))
)
time.sleep(5)

# T8 Print the list of Product Name, Display Price, Link to Product Details Page for each result in results
product_elements = driver.find_elements(By.CLASS_NAME, "_75nlfW")
for product in product_elements:
    name = product.find_element(By.CLASS_NAME, "KzDlHZ").text
    price = product.find_element(By.CLASS_NAME, "_4b5DiR").text
    link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
    print("Product Name:", name)
    print("Product Price:", price)
    print("Link to Product Details Page:", link)
    print()

driver.quit()